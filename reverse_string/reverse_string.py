def reverse_content(content):
    """Recursively reverts the content
    Args:
        content(str): array of letters.
    Returns:
        reversed content.
    """
    if len(content) == 1:
        return content

    return reverse_content(content[1:]) + content[0]


if __name__ == '__main__':
    print(reverse_content('rafael'))

