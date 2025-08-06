def palindrome(text: str):
  """
  >>> print(palindrome("kasur ini rusak"))
  True
  """
  return text == text[::-1]

if __name__ == "__main__":
  import doctest
  doctest.testmod()
