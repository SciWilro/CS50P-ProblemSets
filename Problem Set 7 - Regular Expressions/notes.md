# Notes on using RegEx in python - With VSCode

Regex Previewer extension seems to not be for python. Still looking for alternative

Im also trying [Regex Snippets](https://marketplace.visualstudio.com/items?itemName=Monish.regexsnippets)  
To use start typing `!` and force suggestions by pressing `Ctrl+space` when in python codeblock  

---

Python RegEx functions from `re` module:  

- `re.search` is not anchored `pattern`
    - Ensures the string contains the pattern
    - Can also be used in if statement (Treated as `True` or `False`)
- `re.match` is anchored at the start `^pattern`
    - Ensures the string begins with the pattern
- `re.fullmatch` is anchored at the start and end of the pattern `^pattern$`
    - Ensures the full string matches the pattern
- `re.sub` Find and replace function
- `re.split` Split string on pattern
- `re.findall` Find all instances of a pattern

To make sure python doesnt interpret escape characters we specify the pattern as a raw string ` r'pattern'`  

### RegEx syntax:

| Symbol    | Action      	                |
|-------	|-------------------	        |
| .     	| any character     	        |
| \*    	| 0+ repetitions    	        |
| \+    	| 1+ repetitions    	        |
| ?     	| 0 or 1 repetition 	        |
| {m}   	| m repetitions         	    |
| {m,n} 	| m-n repetitions      	        |
|       	|               	            |
| ^ 	    | matches start of string  	    |
| $     	| matches end of string or before newline |
|       	|               	            |
| [] 	    | set of characters  	        |
| [^]     	| NOT these characters   	    |
|       	|               	            |
| [a-zA-Z]  | Set of all letters            |
| [a\|b]     | a **OR** b                    |
| (...)     | a group                       |
| (?:...)    | non-capturing version         |
|       	|               	            |
| \w      	| words + numbers + _           |
| \W      	| **NOT** words + numbers + _   |
| \d      	| decimal digit                 |
| \D      	| **NOT** decimal digit	        |
| \s      	| whitespace character          |
| \S      	| **NOT** whitespace character  |

`^[A-Z]+`  starts with uppercase character(s) A to Z  
`^[^A-Z]+` starts with any character(s) except uppercase A to Z  
`[\w ]` matches words or spaces. same as `[\w\s]`  
`(@)?\w+` matches '@SciWilro' or just 'SciWilro'  
`(/w\.)+` matches 'mr.wilro' - need to escape .


`flags`: in re.search()
`re.IGNORECASE`  
`re.MULTILINE`  
`re.DOTALL`  

```python
import re
input = "van Niekerk, Wilro"
# Steps to build pattern
matches = re.search(r'.+, .+', input)
matches = re.search(r'^.+, .+$', input)
matches = re.search(r'^(.+), (.+)$', input)
matches = re.search(r'^(.+),\s?(.+)$', input)
if matches:
    fullname = matches.groups()
    last = matches.group(1) # group index starts at 1 - 0 is string
    first = matches.group(2)
    name = f"{first} {last}"
print(f"Hello {name}")
```

Using Walrus operator allows you to assign a re object and test it at same time

```python
input = "van Niekerk, Wilro"
if matches := re.search(r'^(.+),\s?(.+)$', input):
    name = matches.group(2) + ' ' + matches.group(1)

input = 'https://twitter.com/wilro'
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]*)/?", input, re.IGNORECASE):
    print(matches.group(1))
```

Note that `*` and `+` are “greedy,” insofar as “they match as much text as possible,” per [Python Docs RegEx syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax). Adding `?` immediately after either, a la `*?` or `+?`, “makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched.”  

```python
string = 'He said "I havent met any "aliens"."'
pattern = r'(.*?)"(.*)".*'
print(re.search(pattern, string).group(2))
# >>> I havent met any "aliens".

pattern = r'(.*)"(.*)".*'
print(re.search(pattern, string).group(2))
# >>> .
```
