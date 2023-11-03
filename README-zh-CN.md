# android-app-template

[![GitHub license](https://img.shields.io/github/license/BetterAndroid/android-app-template?color=blue)](https://github.com/BetterAndroid/android-app-template/blob/main/LICENSE)
[![Telegram](https://img.shields.io/badge/discussion-Telegram-blue.svg?logo=telegram)](https://t.me/BetterAndroid)
[![Telegram](https://img.shields.io/badge/discussion%20dev-Telegram-blue.svg?logo=telegram)](https://t.me/HighCapable_Dev)

<img src="https://github.com/BetterAndroid/android-app-template/blob/main/img-src/icon.png?raw=true" width = "100" height = "100" alt="LOGO"/>

一个快速创建基础 Android 项目的模版。

[English](https://github.com/BetterAndroid/android-app-template/blob/master/README.md) | 简体中文

| <img src="https://github.com/BetterAndroid/.github/blob/main/img-src/logo.png?raw=true" width = "30" height = "30" alt="LOGO"/> | [BetterAndroid](https://github.com/BetterAndroid) |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |

这个项目属于上述组织，**点击上方链接关注这个组织**，发现更多好项目。

## 这是什么

这是一个快速创建基础 Android 项目的模版，通过此模版，你可以快速创建一个干净、简洁的标准 Android 项目。

模版中自动为你集成了 [BetterAndroid](https://github.com/BetterAndroid/BetterAndroid) 依赖，它能助你的开发变得更轻松。

## 开始使用

在 GitHub 上点击“Use this template”按钮来使用此模版，成功创建新的存储库后，使用 `git clone` 命令将你的项目克隆到本地，此时不要立即打开项目。

在项目的根目录，你可以找到 `initializer.json` 和 `initializer.py` 两个文件，请打开 `initializer.json` 文件，内容如下。

```json
{
  // 你的项目名称，这将作为整个 Gradle 项目的名称，只允许英文
  "__PROJECT_NAME__": "android-app-demo",
  // 你的 App 名称
  "__APP_NAME__": "Android App Demo",
  // 你的项目描述
  "__PROJECT_DESCRIPTION__": "This is a simple Android app demo.",
  // 你的项目存储库 URL (非开源项目可不填并稍后在 gradle.properties 中删除)
  "__PROJECT_URL__": "https://github.com/BetterAndroid/android-app-template",
  // 你的 App 包名
  "__PACKAGE_NAME__": "com.highcapable.androidappdemo",
  // 你的项目许可证名称 (非开源项目可不填并稍后在 gradle.properties 中删除)
  "__LICENCE_NAME__": "Apache License 2.0",
  // 你的项目许可证 URL (非开源项目可不填并稍后在 gradle.properties 中删除)
  "__LICENCE_URL__": "https://github.com/BetterAndroid/android-app-template/blob/main/LICENSE"
}
```

编辑完成配置文件后，运行 `initializer.py` 脚本对项目进行初始化，初始化成功后这两个文件会被自动删除。

如果你的系统中没有 Python，请前往 [官网](https://www.python.org/) 下载一个，然后在命令行执行 `python3 initializer.py`。

如果你正在使用 macOS 或 Linux，你可以直接执行 `./initializer.py`。

项目初始化成功后，你可以使用 Android Studio 或 IntelliJ IDEA 打开这个项目。

## 项目推广

如果你正在寻找一个可以自动管理 Gradle 项目依赖的 Gradle 插件，你可以了解一下 [SweetDependency](https://github.com/HighCapable/SweetDependency) 项目。

如果你正在寻找一个可以自动生成属性键值的 Gradle 插件，你可以了解一下 [SweetProperty](https://github.com/HighCapable/SweetProperty) 项目。

本项目同样使用了 **SweetDependency** 和 **SweetProperty**。

## Star History

![Star History Chart](https://api.star-history.com/svg?repos=BetterAndroid/android-app-template&type=Date)

## 许可证

- [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)

```
Apache License Version 2.0

Copyright (C) 2019-2023 HighCapable

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

版权所有 © 2019-2023 HighCapable