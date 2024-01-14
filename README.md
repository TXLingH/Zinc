# Zinc - 一个开源的,基于 ttkbootstrap 项目的GUI框架

## 介绍
Zinc (锌) 是一个基于ttkbootstrap项目的轻量化GUI框架,使用户能够更多的关注逻辑方面的问题,而不是GUI.

## 如何使用?
很简单,仅仅需要安装前置库ttkbootstrap和Zinc,您就可以在您的项目和代码中使用Zinc.
以下是一个简单的代码示例:

```python
import Zinc
window = Zinc.Window(titleName = "Hello Zinc!")
Zinc.Label(window.window, text = "Hello, Zinc!")
window.launch()