#pragma once

#include "builtins/builtins.hpp"
#include "color/color.hpp"

#include <GLFW/glfw3.h>
#include <gl/GL.h>


class Window {
    GLFWwindow* window;
    string _title;
    int _width, _height;
public:
    Window(
        const string& title, int width, int height
    ) : _title(title), _width(width), _height(height) {
        if (!glfwInit())
            error("Failed to initialize GLFW");

        window = glfwCreateWindow(_width, _height, _title.c_str(), nullptr, nullptr);
        if (window == nullptr) {
            close();
            error("Failed to create GLFW window");
        }
        
        glfwMakeContextCurrent(window);
        glViewport(0, 0, _width, _height);
        glfwSetFramebufferSizeCallback(window, [](GLFWwindow* _, int width, int height) {
            glViewport(0, 0, width, height);
        });
    }

    ~Window() {
        close();
    }

    string title() const { return _title; }
    int width() const { return _width; }
    int height() const { return _height; }
    bool is_running() const { return glfwWindowShouldClose(window); }

    nil close() {
        if (window != nullptr) {
            glfwDestroyWindow(window);
            window = nullptr;
        }
        
        glfwTerminate();
        return nil();
    }

    nil set_bg(const Color& color) const {
        glClearColor(color.r() / 255.0f, color.g() / 255.0f, color.b() / 255.0f, color.a() / 255.0f);
        glClear(GL_COLOR_BUFFER_BIT);
        return nil();
    }

    nil update() const {
        glfwSwapBuffers(window);
        glfwPollEvents();
        return nil();
    }
};

string to_string(const Window& window) {
    return "Window(title='" + window.title() + "', width=" + to_string(window.width()) +
        ", height=" + to_string(window.height()) + ")";
}
