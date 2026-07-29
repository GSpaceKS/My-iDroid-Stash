#!/usr/bin/env python3
"""
每半月更新：NB助手、unc0ver、checkra1n、iMazing
统一使用 Badge 展示版本号
"""

import re
import os
import requests
import subprocess

README = "README.md"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def get_nb_version():
    url = "https://nbtool.lanzn.com/nbtool-win64"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
    except requests.exceptions.Timeout:
        raise Exception("NB助手连接超时")
    resp.encoding = 'utf-8'
    match = re.search(r'nbtool-(\d+\.\d+\.\d+\.\d+)-win64\.exe', resp.text)
    if match:
        return match.group(1)
    raise Exception("NB助手 版本未找到")

def get_unc0ver_version():
    url = "https://unc0ver.dev/"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.encoding = 'utf-8'
    match = re.search(r'v(\d+\.\d+\.\d+)', resp.text)
    if match:
        return f"v{match.group(1)}"
    raise Exception("unc0ver 版本未找到")

def get_checkra1n_version():
    url = "https://checkra.in/releases/"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.encoding = 'utf-8'
    text = resp.text
    match = re.search(r'checkra1n\s+(\d+\.\d+\.\d+)\s+beta', text)
    if match:
        return f"{match.group(1)} beta"
    match = re.search(r'checkra1n\s+(\d+\.\d+\.\d+)', text)
    if match:
        return match.group(1)
    raise Exception("checkra1n 版本未找到")

def get_imazing_version():
    url = "https://imazing.com/download"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.encoding = 'utf-8'
    text = resp.text
    match = re.search(r'Version:</p>\s*<p><b>([\d.]+)</b></p>', text, re.DOTALL)
    if match:
        return match.group(1)
    match = re.search(r'Version:\s*([\d.]+)', text, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r'<p><b>([\d.]+)</b></p>', text)
    if match:
        return match.group(1)
    raise Exception("iMazing 版本未找到")

def make_badge(version_str):
    ver_match = re.search(r'(\d+\.\d+\.\d+\.?\d*)', version_str)
    if not ver_match:
        ver_match = re.search(r'(\d+\.\d+)', version_str)
    if not ver_match:
        return version_str
    ver = ver_match.group(1)
    is_beta = 'beta' in version_str.lower()
    label = 'beta' if is_beta else 'release'
    color = 'orange' if is_beta else 'blue'
    badge_url = f"https://img.shields.io/badge/{label}-v{ver}-{color}"
    return f"![{label}]({badge_url})"

def update_readme(project_name, new_version):
    if new_version is None:
        print(f"⏭️ {project_name} 跳过更新（无版本信息）")
        return False

    with open(README, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    updated = False
    new_lines = []
    badge = make_badge(new_version)

    for line in lines:
        if project_name in line and '|' in line:
            parts = line.split('|')
            if len(parts) >= 5:
                parts[-2] = badge
                new_line = '|'.join(parts)
                if new_line != line:
                    updated = True
                    line = new_line
        new_lines.append(line)

    if updated:
        with open(README, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"✅ 已更新 {project_name} 版本为 {new_version} (Badge)")
        return True
    else:
        print(f"⏭️ {project_name} 版本无变化")
        return False

def biweekly_update():
    projects = [
        {"name": "NB助手", "get": get_nb_version},
        {"name": "unc0ver", "get": get_unc0ver_version},
        {"name": "checkra1n", "get": get_checkra1n_version},
        {"name": "iMazing", "get": get_imazing_version},
    ]

    any_updated = False
    for p in projects:
        try:
            ver = p["get"]()
            if update_readme(p["name"], ver):
                any_updated = True
        except Exception as e:
            print(f"❌ 获取 {p['name']} 版本失败: {e}")

    return any_updated

if __name__ == "__main__":
    if biweekly_update():
        if os.path.exists('.git'):
            subprocess.run(["git", "config", "user.email", "action@github.com"], check=False)
            subprocess.run(["git", "config", "user.name", "GitHub Action"], check=False)
            subprocess.run(["git", "add", README], check=False)
            subprocess.run(["git", "commit", "-m", "biweekly: update versions (Badge)"], check=False)
            subprocess.run(["git", "push"], check=False)