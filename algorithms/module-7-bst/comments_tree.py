class CommentNode:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "This comment has been removed."
        self.is_deleted = True

    def display(self, indent=0):
        if not self.is_deleted:
            print(" " * indent + f"{self.author}: {self.text}")
        else:
            print(" " * indent + "This comment has been removed.")
        for reply in self.replies:
            reply.display(indent + 4)


class CommentTree:
    def __init__(self, root: CommentNode):
        self.root = root

    def display(self):
        if self.root:
            self.root.display()

    def sum_comments(self):
        return self._sum_comments(self.root) - 1

    def _sum_comments(self, node: CommentNode):
        if node is None:
            return 0
        total_sum = 1
        for reply in node.replies:
            total_sum += self._sum_comments(reply)

        return total_sum


if __name__ == "__main__":
    root_comment = CommentNode("What a wonderful book!", "Bodja")
    reply1 = CommentNode("The book is a total disappointment :(", "Andriy")
    reply2 = CommentNode("What's so wonderful about it?", "Marina")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = CommentNode("Not a book, just wasted paper...", "Serhiy")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    comment_tree = CommentTree(root_comment)

    print("\nComment Tree Structure:")
    comment_tree.display()

    print("\nTotal number of comments and replies:", comment_tree.sum_comments())
