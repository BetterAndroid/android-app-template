# android-app-template

[![GitHub license](https://img.shields.io/github/license/BetterAndroid/android-app-template?color=blue)](https://github.com/BetterAndroid/android-app-template/blob/main/LICENSE)
[![Telegram](https://img.shields.io/badge/discussion-Telegram-blue.svg?logo=telegram)](https://t.me/BetterAndroid)
[![Telegram](https://img.shields.io/badge/discussion%20dev-Telegram-blue.svg?logo=telegram)](https://t.me/HighCapable_Dev)

<img src="https://github.com/BetterAndroid/android-app-template/blob/main/img-src/icon.png?raw=true" width = "100" height = "100" alt="LOGO"/>

A template for quickly creating basic Android project.

English | [简体中文](https://github.com/BetterAndroid/android-app-template/blob/main/README-zh-CN.md)

| <img src="https://github.com/BetterAndroid/.github/blob/main/img-src/logo.png?raw=true" width = "30" height = "30" alt="LOGO"/> | [BetterAndroid](https://github.com/BetterAndroid) |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |

This project belongs to the above-mentioned organization, **click the link above to follow this organization** and discover more good projects.

## What's this

This is a template for quickly creating a basic Android project.

Through this template, you can quickly create a clean and concise standard Android project.

The template automatically integrates the [BetterAndroid](https://github.com/BetterAndroid/BetterAndroid) dependency for you, which can help make your development easier.

## Get Started

Click the "Use this template" button on GitHub to use this template.

After successfully creating a new repository, use the `git clone` command to clone your project locally, do not open the project immediately at this time.

In the root directory of the project, you can find two files, `initializer.json` and `initializer.py`, please open the `initializer.json` file, the contents are as follows.

```json
{
   // Your project name, this will be used as the name of the entire Gradle project, only English is allowed
   "__PROJECT_NAME__": "android-app-demo",
   // Your app name
   "__APP_NAME__": "Android App Demo",
   // Your project description
   "__PROJECT_DESCRIPTION__": "This is a simple Android app demo.",
   // Your project repository URL (can be left blank for non-open source projects and deleted in gradle.properties later)
   "__PROJECT_URL__": "https://github.com/BetterAndroid/android-app-template",
   // Your app package name
   "__PACKAGE_NAME__": "com.highcapable.androidappdemo",
   // Your project license name (for non-open source projects, you can leave it blank and delete it in gradleproperties later)
   "__LICENCE_NAME__": "Apache License 2.0",
   // Your project license URL (for non-open source projects, you can leave it blank and delete it later in gradle.properties)
   "__LICENCE_URL__": "https://github.com/BetterAndroid/android-app-template/blob/main/LICENSE"
}
```

After editing the configuration file, run the `initializer.py` script to initialize the project, after successful initialization, these two files will be automatically deleted.

If there is no Python in your system, please go to [official website](https://www.python.org/) to download one, and then execute `python3 initializer.py` on the command line.

If you are using macOS or Linux, you can execute `./initializer.py` directly.

After the project is initialized successfully, you can use Android Studio or IntelliJ IDEA to open the project.

## Promotion

If you are looking for a Gradle plugin that can automatically manage Gradle project dependencies,
you can check out the [SweetDependency](https://github.com/HighCapable/SweetDependency) project.

If you are looking for a Gradle plugin that can automatically generate properties key-values,
you can check out the [SweetProperty](https://github.com/HighCapable/SweetProperty) project.

This project also uses **SweetDependency** and **SweetProperty**.

## Star History

![Star History Chart](https://api.star-history.com/svg?repos=BetterAndroid/android-app-template&type=Date)

## License

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

Copyright © 2019-2023 HighCapable