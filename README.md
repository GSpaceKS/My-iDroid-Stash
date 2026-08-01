# My iDroid Stash
**归档自用**

``` text
使用 GitHub Action 搭配自己写的 Python 脚本来获取版本号
其中，每天 (UTC 00：00) 获取版本号的是 MT管理器、Sideloadly、爱思助手、沙漏验机
每半个月 (每月1号和16号的 UTC 00：00) 获取版本号的是 Scene、unc0ver、checkra1n、iMazing
```

> **由于 NB助手 官网没有写版本号，且蓝奏云反爬限制，无法进行版本号获取**

## 索引

- [Android](#android)
    - [权限类](#权限类)
    - [工具类](#工具类)
- [iOS](#ios)
    - [工具类](#工具类-1)
    - [Jailbreak](#jailbreak)
    - [自签](#自签)

---

## Android

> ## 权限类

| 图标 | 工具 | 官方地址 | 下载链接 | 版本 | 介绍 |
|-|-|-|-|-|-|
| <img src="icons/Android/Permission/Shizuku.png" width="24"> | Shizuku | [官网](https://shizuku.rikka.app/zh-hans/) | [GitHub Releases](https://github.com/RikkaApps/Shizuku/releases) | ![Shizuku 最新版本](https://img.shields.io/github/v/release/RikkaApps/Shizuku) | 无需Root，为应用提供ADB级权限的中间件 |
| <img src="icons/Android/Permission/Shizuku_thedjchi.png" width="24"> | Shizuku (FORK) | [GitHub](https://github.com/thedjchi/Shizuku) | [GitHub Releases](https://github.com/thedjchi/Shizuku/releases) | ![Shizuku (FORK) 最新版本](https://img.shields.io/github/v/release/thedjchi/Shizuku) | Shizuku 的个人维护分支 |
| <img src="icons/Android/Permission/Dhizuku.png" width="24"> | Dhizuku | [GitHub](https://github.com/iamr0s/Dhizuku) | [GitHub Releases](https://github.com/iamr0s/Dhizuku/releases) | ![Dhizuku 最新版本](https://img.shields.io/github/v/release/iamr0s/Dhizuku) | 类似 Shizuku，但分享的是设备所有者权限 |
| <img src="icons/Android/Permission/Magisk.png" width="24"> | Magisk | [官网](https://magisk.me/) | [GitHub Releases](https://github.com/topjohnwu/Magisk/releases) | ![ 最新版本](https://img.shields.io/github/v/release/topjohnwu/Magisk) | 不修改系统分区的Root框架 |
| <img src="icons/Android/Permission/KernelSU.png" width="24"> | KernelSU | [官网](https://kernelsu.org/zh_CN/) | [GitHub Releases](https://github.com/tiann/KernelSU/releases) | ![KernelSU 最新版本](https://img.shields.io/github/v/release/tiann/KernelSU) | 无需修补Boot镜像，内核级Root框架 |

---

> ## 工具类

| 图标 | 工具 | 官方地址 | 下载链接 | 版本 | 介绍 |
|-|-|-|-|-|-|
| <img src="icons/Android/Tools/Obtainium.png" width="24"> | Obtainium | [GitHub](https://github.com/ImranR98/Obtainium) | [GitHub Releases](https://github.com/ImranR98/Obtainium/releases) | ![Obtainium 最新版本](https://img.shields.io/github/v/release/ImranR98/Obtainium) | 侧载应用更新器 |
| <img src="icons/Android/Tools/Scene.png" width="24"> | Scene | [官网](https://omarea.com/#/) | [官网下载](https://omarea.com/#/platform) |![release](https://img.shields.io/badge/release-v9.3.8-blue)| 手机性能调控工具箱 |
| <img src="icons/Android/Tools/LibChecker.png" width="24"> | LibChecker | [GitHub](https://github.com/LibChecker/LibChecker) | [GitHub Releases](https://github.com/LibChecker/LibChecker/releases) | ![LibChecker 最新版本](https://img.shields.io/github/v/release/LibChecker/LibChecker) | 解析APK，看内部组件和引用的SDK |
| <img src="icons/Android/Tools/Hail.png" width="24"> | 雹 (Hail) | [GitHub](https://github.com/aistra0528/Hail) | [GitHub Releases](https://github.com/aistra0528/Hail/releases) | ![雹 (Hail) 最新版本](https://img.shields.io/github/v/release/aistra0528/Hail) | 配合Shizuku/Dhizuku可免Root冻结任意App |
| <img src="icons/Android/Tools/App_Manager.png" width="24"> | App Manager | [GitHub](https://github.com/MuntashirAkon/AppManager) | [GitHub Releases](https://github.com/MuntashirAkon/AppManager/releases) | ![App Manager 最新版本](https://img.shields.io/github/v/release/MuntashirAkon/AppManager) | 查看/管理App所有组件和权限 |
| <img src="icons/Android/Tools/mt2.png" width="24"> | MT管理器 | [官网](https://mt2.cn/) | [官网下载](https://mt2.cn/download/) |![release](https://img.shields.io/badge/release-v2.26.7-blue)| 双窗口文件管理+直接修改APK |
| <img src="icons/Android/Tools/InstallerX_Revived.png" width="24"> | InstallerX Revived | [GitHub](https://github.com/wxxsfxyzm/InstallerX-Revived) | [GitHub Releases](https://github.com/wxxsfxyzm/InstallerX-Revived/releases) | ![InstallerX Revived 最新版本](https://img.shields.io/github/v/release/wxxsfxyzm/InstallerX-Revived) | 原 InstallerX 的社区续作，开源安装器 |
| <img src="icons/Android/Tools/SAI.png" width="24"> | SAI | [GitHub](https://github.com/Aefyr/SAI) | [GitHub Releases](https://github.com/Aefyr/SAI/releases) | ![SAI 最新版本](https://img.shields.io/github/v/release/Aefyr/SAI) | 专治各种分包格式的开源安装器 |
| <img src="icons/Android/Tools/Image_Toolbox.png" width="24"> | Image Toolbox | [GitHub](https://github.com/T8RIN/ImageToolbox) | [GitHub Releases](https://github.com/T8RIN/ImageToolbox/releases) | ![Image Toolbox 最新版本](https://img.shields.io/github/v/release/T8RIN/ImageToolbox) | 开源免费无广告的全能图片处理工具 |
| <img src="icons/Android/Tools/aShellYou.png" width="24"> | aShell You | [GitHub](https://github.com/DP-Hridayan/aShellYou) | [GitHub Releases](https://github.com/DP-Hridayan/aShellYou/releases) | ![aShell You 最新版本](https://img.shields.io/github/v/release/DP-Hridayan/aShellYou) | 手机上的ADB命令行工具 |
| <img src="icons/Android/Tools/Termux.png" width="24"> | Termux | [官网](https://termux.dev/cn/) | [GitHub Releases](https://github.com/termux/termux-app/releases) | ![Termux 最新版本](https://img.shields.io/github/v/release/termux/termux-app) | 开源终端模拟器+包管理器 |

## iOS

> ## 工具类

| 图标 | 工具 | 官方地址 | 下载链接 | 版本 | 介绍 |
|-|-|-|-|-|-|
| <img src="icons/iOS/Tools/iTunes.png" width="24"> | iTunes | [官网](https://www.apple.com.cn/itunes/) | [Microsoft Store](https://apps.microsoft.com/detail/9pb2mz1zmb1s?hl=zh-CN&gl=CN) / [普通安装包](https://www.apple.com/itunes/download/win64) | — (Microsoft Store) | 苹果设备管理软件 |
| <img src="icons/iOS/Tools/iCloud.png" width="24"> | iCloud | [官网](https://www.icloud.com/) | [Microsoft Store](https://apps.microsoft.com/detail/9pktq5699m62?hl=zh-CN&gl=CN) / [普通安装包 (2020 老版本)](https://updates.cdn-apple.com/2020/windows/001-39935-20200911-1A70AA56-F448-11EA-8CC0-99D41950005E/iCloudSetup.exe) | — (Microsoft Store) | 苹果云存储 |
| <img src="icons/iOS/Tools/i4.png" width="24"> | 爱思助手 | [官网](https://i4.cn/) | [官网下载](https://i4.cn/) |![release](https://img.shields.io/badge/release-v9.16-blue)| 刷机/备份/装应用一站式管理 |
| <img src="icons/iOS/Tools/shalou.png" width="24"> | 沙漏验机 | [官网](https://www.shalou.net/#/home) | [官网下载](https://www.shalou.net/#/home) |![release](https://img.shields.io/badge/release-v8.1.0-blue)| 验机/刷机/管理苹果设备 |
| <img src="icons/iOS/Tools/iMazing.png" width="24"> | iMazing | [官网](https://imazing.com/) | [官网下载](https://imazing.com/) |![release](https://img.shields.io/badge/release-v3.6.2-blue)| 备份/传文件/管理iPhone的电脑软件 |

---

> ## Jailbreak

| 图标 | 工具 | 官方地址 | 下载链接 | 版本 | 介绍 |
|-|-|-|-|-|-|
| <img src="icons/iOS/Jailbreak/Dopamine.png" width="24"> | Dopamine | [官网](https://dopamine.dhinak.net/) | [GitHub Releases](https://github.com/opa334/Dopamine/releases) | ![Dopamine 最新版本](https://img.shields.io/github/v/release/opa334/Dopamine) | 开源、无根、半不完美越狱 |
| <img src="icons/iOS/Jailbreak/palera1n.png" width="24"> | palera1n | [官网](https://palera.in/) | [GitHub Releases](https://github.com/palera1n/palera1n/releases) | ![palera1n 最新版本](https://img.shields.io/github/v/release/palera1n/palera1n) | checkm8硬件漏洞越狱 |
| <img src="icons/iOS/Jailbreak/unc0ver.png" width="24"> | unc0ver | [官网](https://unc0ver.dev/) | [官网下载](https://unc0ver.dev/) |![release](https://img.shields.io/badge/release-v4.3.1-blue)| 半不完美越狱，支持 Cydia，最高到 iOS 14.8 |
| <img src="icons/iOS/Jailbreak/Taurine.png" width="24"> | Taurine | [官网](https://taurine.app/) | [GitHub Releases](https://github.com/Odyssey-Team/Taurine/releases) | ![Taurine 最新版本](https://img.shields.io/github/v/release/Odyssey-Team/Taurine) | Odyssey 团队开发的越狱工具 (iOS 14.0-14.8.1) |
| <img src="icons/iOS/Jailbreak/Odyssey.png" width="24"> | Odyssey | [官网](https://theodyssey.dev/) | [GitHub Releases](https://github.com/Odyssey-Team/Odyssey/releases) | ![ 最新版本](https://img.shields.io/github/v/release/Odyssey-Team/Odyssey) | CoolStar 团队开发的 iOS 13 越狱工具 |
| <img src="icons/iOS/Jailbreak/checkra1n.png" width="24"> | checkra1n | [官网](https://checkra.in/) | [官网下载](https://checkra.in) |![beta](https://img.shields.io/badge/beta-v0.12.4-orange)| checkm8漏洞的经典越狱工具 |

> ### Jailbreak 版本说明 (使用AI总结，iOS对应版本可能有误，请对照查看)
| 软件 | 最新版本 | 支持的处理器 | 支持的iOS版本 | 项目状态 | 备注 |
|-|-|-|-|-|-|
| **Dopamine** | v2.4.9 | A9–A11 (arm64) | iOS 15.0 – 15.8.6 / 16.0 – 16.6.1 | 活跃维护 | 官方 GitHub: opa334/Dopamine；v2.5 beta 已扩展至 iOS 17.0–17.3.1 |
|  |  | A12–A16, M1–M2 (arm64e) | iOS 15.0 – 16.5.1 |  |  |
| **palera1n** | v2.4 | A8 – A11 | iOS/iPadOS 15.0 – 18.7.9 (有争议，最高可能至17.4.1) | 活跃维护 | 基于 checkm8 硬件漏洞；A11 设备需禁用锁屏密码；iOS 16 以上可能需要抹掉数据；需 macOS/Linux |
| **unc0ver** | v8.0.2 | v6.0.0: A8–A13 | iOS 11.0 – 14.3 | **已停止维护** | 官方 GitHub 已归档；不同版本对芯片支持有差异 |
|  |  | v8.0.0+: **仅 A12–A13** | iOS 14.6 – 14.8 |  |  |
| **Taurine** | v1.1.7-3 | A8 – A14 | iOS/iPadOS 14.0 – 14.8.1 | **已停止维护** (归档) | Odyssey Team 开发；官方 GitHub 已归档 |
| **Odyssey** | v1.4.3 | A8 – A13 | iOS 13.0 – 13.7 | **已停止维护** (归档) | **不兼容** iOS 13.5.1 和 13.6；官方 GitHub 已归档 |
| **checkra1n** | 0.12.4 beta | A5 – A11 | 官方: iOS 12.0 – 14.8.1 | 活跃维护 | 基于 checkm8 硬件漏洞；A11 + iOS 14.0+ 需禁用锁屏密码；需 macOS/Linux |
|  |  | A9–A11 | 实验性: iOS 15 – 16 |  | 实验性支持，非官方正式版 |

---

> ## 自签

| 图标 | 工具 | 官方地址 | 下载链接 | 版本 | 介绍 |
|-|-|-|-|-|-|
| <img src="icons/iOS/Sign/TrollStore.png" width="24"> | TrollStore | [GitHub](https://github.com/opa334/TrollStore) | [GitHub Releases](https://github.com/opa334/TrollStore/releases) | ![TrollStore 最新版本](https://img.shields.io/github/v/release/opa334/TrollStore) | opa334开发的永久签名安装器 (CoreTrust漏洞) |
| <img src="icons/iOS/Sign/AltStore.png" width="24"> | AltStore (需要 Windows / MacOS) | [官网](https://altstore.io/) | [GitHub Releases](https://github.com/altstoreio/AltStore/tags) | ![AltStore 最新版本](https://img.shields.io/github/v/tag/altstoreio/AltStore) | 电脑配合，7天自动续签装IPA |
| <img src="icons/iOS/Sign/Sideloadly.png" width="24"> | Sideloadly (需要 Windows / MacOS) | [官网](https://sideloadly.io/) | [官网下载](https://sideloadly.io/) |![release](https://img.shields.io/badge/release-v0.60.0-blue)| 比AltStore更灵活，Win/Mac都能用，支持USB+WiFi |
| <img src="icons/iOS/Sign/nbtool8.png" width="24"> | NB助手 (需要 Windows / MacOS) | [官网](https://nbtool8.com/) | [官网下载](https://nbtool8.com/) | 没办法自动更新，截至2026/7/30，最新 Windows 版本是 v2.4.0.0 | 国产免费iOS IPA签名+应用管理工具，但首次需电脑 |
| <img src="icons/iOS/Sign/ios222.png" width="24"> | 牛蛙助手 (需要 Windows / MacOS) | [官网](https://ios222.com/) | [官网下载](https://ios222.com/) | 已停止更新，最新为 v1.1.2 | 和NB助手类似，首次需电脑，后续手机续签 |

---

### [↑ 回到顶部](#my-idroid-stash)