# class book_data:
#     def __init__(self, title=None, author=None, mamabar=None):
#         self.title = title
#         self.author = author
#         self.mamabar = mamabar
#         self.book_data = {}
#         self.pak()
#
#     def pak(self):
#         try:
#             self.title = 3 / 0
#             self.author = 2 / 1
#             self.mamabar = 4
#         except(ZeroDivisionError):
#             pass
#         self.book_data = {
#             'title': self.title,
#             'author': self.author,
#             'mamabar': self.mamabar
#         }
#         print(self.book_data)

param='Масса: --474 г'
wheith=''.join([i for i in param if i.isdigit()])
print(wheith)
