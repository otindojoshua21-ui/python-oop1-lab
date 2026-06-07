#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1

    def turn_page(self):
        if self.current_page < self.pages:
            self.current_page += 1
            return f"Turned to page {self.current_page} of '{self.title}'."
        else:
            return f"You have reached the end of '{self.title}'."