import os
import sys
import json
import base64
import argparse
import requests
import re

def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            ext = os.path.splitext(image_path)[1].lower().replace('.', '')
            if ext == 'jpg': ext = 'jpeg'
            return f"data:image/{ext};base64,{encoded_string}"
    except Exception as e:
        print(f"Error reading image: {e}", file=sys.stderr)
        return None

def generate(prompt, model, image_path, api_base, api_key, stream=True):
    if not api_base or not api_key:
        print("Error: Missing API base URL or API key.", file=sys.stderr)
        return

    content = []
    if prompt:
        content.append({"type": "text", "text": prompt})
    
    if image_path:
        data_url = get_image_base64(image_path)
        if data_url:
            content.append({"type": "image_url", "image_url": {"url": data_url}})

    body = {
        "model": model,
        "messages": [{"role": "user", "content": content}],
        "stream": stream
    }

    url = f"https://vip.yyds168.net/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        if stream:
            response = requests.post(url, headers=headers, json=body, stream=True)
            response.raise_for_status()
            
            full_content = ""
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8').strip()
                    if decoded_line.startswith("data:"):
                        payload = decoded_line[5:].strip()
                        if payload == "[DONE]":
                            break
                        try:
                            data = json.loads(payload)
                            delta = data.get("choices", [{}])[0].get("delta", {})
                            chunk = delta.get("content", "")
                            if chunk:
                                full_content += chunk
                        except:
                            continue
            
            img_match = re.search(r"!\[[^\]]*\]\(([^\)]+)\)", full_content)
            video_match = re.search(r"<video[^>]*src=['\"]([^'\"]+)['\"][^>]*>", full_content, re.IGNORECASE)
            
            if img_match:
                print(f"Generated Image: {img_match.group(1)}")
            elif video_match:
                print(f"Generated Video: {video_match.group(1)}")
            else:
                print("Generation complete, but no media URL found in the response.")
                print(f"Response content: {full_content}")
        else:
            response = requests.post(url, headers=headers, json=body)
            response.raise_for_status()
            data = response.json()
            content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
            print(content)
            
    except Exception as e:
        print(f"API request failed: {e}", file=sys.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate images/videos using f2aTools (YYDS API)")
    parser.add_argument("--prompt", required=True, help="Prompt for generation")
    parser.add_argument("--model", default="gemini-2.5-flash-image-landscape", help="Model name")
    parser.add_argument("--image_path", help="Path to local reference image")
    parser.add_argument("--api_base", default="https://vip.yyds168.net", help="API Base URL")
    parser.add_argument("--api_key", default=os.getenv("VITE_API_KEY") or os.getenv("F2A_API_KEY"), help="API Key")
    
    args = parser.parse_args()
    
    generate(args.prompt, args.model, args.image_path, args.api_base, args.api_key)
