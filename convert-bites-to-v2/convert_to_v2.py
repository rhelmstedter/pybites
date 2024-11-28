import pathlib
import json
import requests

BITES_API = "https://pybitesplatform.com/api/bites/"
URL_BASE = "https://pybitesplatform.com/bites/"
BITES = """Bite 1. Sum n numbers
Bite 5. Parse a list of names
Bite 8. Rotate string characters
Bite 15. Enumerate 2 sequences
Bite 16. PyBites date generator
Bite 19. Write a property
Bite 21. Query a nested data structure
Bite 26. Dictionary comprehensions are awesome
Bite 29. Martin's IQ test
Bite 32. Don't let mutability fool you
Bite 37. Rewrite a for loop using recursion
Bite 38. Using ElementTree to parse XML
Bite 43. Force keyword arguments
Bite 44. License key generator
Bite 45. Keep a queue of last n items
Bite 46. You are a programmer! Code Fizz Buzz
Bite 54. Nicer formatting of a poem or text
Bite 55. Get the latest game releases from Steam's RSS feed
Bite 56. Add a command line interface to our BMI calculator
Bite 64. Fix a truncating zip function
Bite 66. Calculate the running average of a sequence
Bite 67. Working with datetimes
Bite 68. Remove punctuation characters from a string
Bite 74. What day of the week were you born on?
Bite 77. New places to travel to
Bite 80. Check equality of two lists
Bite 83. At what time does PyBites live?
Bite 91. Matching multiple strings
Bite 96. Build Unix' wc program in Python
Bite 100. Display the last part of a file (Unix tail)
Bite 115. Count leading spaces
Bite 117. Round a number even (a.k.a. banker's rounding)
Bite 128. Work with datetime's strptime and strftime
Bite 130. Analyze some basic Car Data
Bite 133. Convert an Amazon URL into an affiliation link
Bite 136. Bloodtypes
Bite 143. Look up a value in 3 dictionaries
Bite 149. Sorting words with constraint
Bite 153. Round a sequence of numbers
Bite 161. Count the number of files and directories
Bite 165. Parse an /etc/passwd file output
Bite 167. Complete a User class: properties and representation dunder methods
Bite 169. Simple length converter
Bite 172. Having fun with Python Partials
Bite 176. Create a variable length chessboard
Bite 180. Group names by country
Bite 181. Keep a list sorted upon insert
Bite 188. Get statistics from PyBites test code
Bite 189. Filter a list of names
Bite 192. Some logging practice
Bite 208. Find the number pairs summing up N
Bite 209. Write a Sphinx docstring
Bite 210. Add Type Annotations
Bite 214. A countdown generator
Bite 215. Validate a license key
Bite 218. Create a sandwich decorator
Bite 225. Swap case PyBites characters
Bite 231. Where are the emojis?
Bite 238. Write tests for Fibonacci
Bite 241. Write tests for list_to_decimal
Bite 246. Test print / standard output
Bite 251. Introducing Pandas Series
Bite 252. Let's play with Pandas Series
Bite 254. Global vs local variables
Bite 257. Extract users dict from a multiline string
Bite 262. GC content
Bite 270. Most frequent digit in number
Bite 278. Major and minor numbers
Bite 279. Armstrong numbers
Bite 283. Like there's no tomorrow?
Bite 288. Smallest number
Bite 289. Round to next number
Bite 293. N digit numbers
Bite 295. Join lists
Bite 314. Print names to columns
Bite 317. Pickling objects
Bite 318. Decode base64 encoded data
Bite 319. Identity and equality
Bite 322. Reading progress
Bite 323. Iterables intersection
Bite 324. Pretty string
Bite 336. FastAPI Hello World
Bite 337. A little detour: Pydantic
Bite 347. Which words can you type with one hand?
Bite 353. Transform a Script Into a Command Line Interface (CLI)
Bite 355. Create Your First Typer Command Line Interface (CLI) Application
Bite 357. Implement your First Subcommands and Command Groups
Bite 360. Add a progress bar to Your Command Line Interface (CLI)
Bite 371. Python3.9 - Dictionary Merge
Bite 372. Validate Pangram
Bite 373. Reverse only Letters
Bite 3. Word Values
Bite 4. Top 10 PyBites tags
Bite 6. PyBites Die Hard
Bite 7. Parsing dates from logs
Bite 9. Palindromes
Bite 10. Practice exceptions
Bite 12. Write a user validation function
Bite 13. Convert dict to namedtuple/json
Bite 14. Generate a table of n sequences
Bite 17. Form teams from a group of friends
Bite 18. Find the most common word
Bite 22. Write a decorator with argument
Bite 25. No promo twice, keep state in a class
Bite 27. Parse omdb movie json data
Bite 28. Converting date strings to datetimes
Bite 30. Movie data analysis
Bite 33. Transpose a data structure
Bite 35. Having fun with heapq
Bite 36. Having fun with *args and **kwargs
Bite 39. Calculate the total duration of a course
Bite 41. Write a login_required decorator
Bite 47. Write a new password field validator
Bite 48. Make a bar chart of new Safari books
Bite 49. Scrape Packt's html with BeautifulSoup
Bite 51. When does Python 2 die on Planet Miller?
Bite 57. Create a simple calculator that receives command line arguments
Bite 59. Create a multiplication table class of variable length
Bite 60. Create a deck of Uno cards
Bite 62. Data structures matter - speed up your Python code
Bite 65. Get all valid dictionary words for a draw of letters
Bite 70. Create your own iterator
Bite 71. Keep state in a class + make its instance callable
Bite 72. Retrieve the right Ninja Belt based on score
Bite 73. Organize a meeting between timezones (pytz)
Bite 78. Find programmers with common languages
Bite 79. Parse a csv file and create a bar chart
Bite 81. Filter and order tweets by polarity values
Bite 82. Define a Score Enum and customize  it adding methods
Bite 84. Flatten lists recursively (Droste Bite)
Bite 86. Create a RGB-to-Hex converter
Bite 87. Convert Decimal to Roman Numerals
Bite 89. Playing with lists and dicts
Bite 90. What South Park characters talk most?
Bite 92. Humanize a datetime
Bite 95. Subclass the dict built-in
Bite 97. BeautifulSoup II - scrape US holidays
Bite 99. Write an infinite sequence generator
Bite 111. Use the ipinfo API to lookup IP country
Bite 113. Filter words with non-ascii characters
Bite 114. Implement a Color class with staticmethod
Bite 116. List and filter files in a directory
Bite 118. List exercise: return first occurrence indices of duplicated words
Bite 119. Xmas tree generator
Bite 120. Write a numbers validation decorator
Bite 122. Check if two words are anagrams
Bite 123. Find the user with most friends
Bite 125. Get the most recommended books
Bite 127. Return the right ordinal suffix for a number
Bite 129. Analyze Stock Data
Bite 132. Find the word with the most vowels
Bite 135. Sort a list of book objects
Bite 137. Gourmets' Nightmare
Bite 138. OOP fun at the Zoo
Bite 140. PyBites First Pandas Bite
Bite 141. Primitive date format inferrer
Bite 142. Exception Handling: Calculate the Winning Player
Bite 144. Calculate the Number of Months Passed
Bite 146. Rhombus generator
Bite 147. 100 WEEKDays of Code Date Range
Bite 148. Print Car Data Grouped by Manufacturer
Bite 150. Turn messy CSV into JSON
Bite 151. Contemporary Composers
Bite 154. Write your own Data Class
Bite 155. Split a string by spaces or quoted text
Bite 156. Make an index of story characters
Bite 157. Filter out accented characters
Bite 159. Create a simple calculator
Bite 162. Vertically align output of counters
Bite 163. Which packages were upgraded?
Bite 166. Complete a tox ini file parser class
Bite 173. Set up future notifications
Bite 175. Find missing dates
Bite 178. Parse PyBites blog git commit log
Bite 182. Parse a bunch of quotes from HTML
Bite 184. Analyze some Bite stats data
Bite 185. Create a simple spelling suggester
Bite 186. Calculate number of books to have read at date ...
Bite 187. Actor/actress age at movie release
Bite 190. Parse income distribution from Latin America XML
Bite 191. Starwars character with highest BMI
Bite 193. Most upvoted StackOverflow Python questions
Bite 194. Add caching to a Fibonacci function
Bite 195. Analyze NBA Data with sqlite3
Bite 197. What date is Mother's Day celebrated?
Bite 199. Multiple inheritance (__mro__)
Bite 201. Call a Cisco Nexus 9k device
Bite 202. Analyze some Bite stats data - part II
Bite 203. Add type hints to a class
Bite 205. Female speakers @ Pycon US
Bite 206. Calculate and evenly split the bill
Bite 212. Suppressing exceptions
Bite 217. Capture stdout
Bite 219. Bite notification planner
Bite 221. Parse best selling lists using the NY Times API
Bite 222. Split an iterable in groups of size n
Bite 223. Unix file permissions
Bite 226. Get top titles from news.python.sc
Bite 227. Convert Warcraft json data to csv
Bite 228. Create a Gravatar URL
Bite 230. Thumbs up for operator overloading
Bite 232. Analyze gold prices
Bite 233. Make a zipfile of the latest log files
Bite 234. Capitalize sentences
Bite 235. Which Bite has the fastest tests?
Bite 236. User experience matters! Suggest matching files
Bite 239. Test FizzBuzz
Bite 243. Test code that parses JSON and IP ranges
Bite 244. Make mutpy's output more digestible
Bite 245. Xmas Tree 2.0
Bite 247. Mocking a standard library function
Bite 253. More Pandas Series Practice
Bite 255. Codon Usage
Bite 256. Scrape PyCon events
Bite 258. What the flux?
Bite 259. Reverse complement
Bite 261. Visit all PyCons in Europe
Bite 263. Count the number of islands in a grid
Bite 264. Clamy Fernet
Bite 265. Optimal fund raising
Bite 267. Measure the size of an island
Bite 271. Get all class names from a module
Bite 272. Find common words
Bite 274. Number conversion problem
Bite 275. Get the most common email domains
Bite 284. Pascal triangle
Bite 285. Nested List Extraction
Bite 286. Decompress
Bite 287. Sum indices
Bite 290. Class Rosters Data Conversion
Bite 291. Find the fastest speech
Bite 296. Jagged list
Bite 298. Fasta to 2-Line Fasta
Bite 299. Base converter
Bite 301. Exchange rates
Bite 302. Get and write all code from a JSON file
Bite 304. Most identical letters in a word
Bite 305. Split once, delimit many
Bite 306. Translate coding sequences to proteins
Bite 307. SQLite3 introduction
Bite 308. Calculate the median from a dictionary
Bite 309. A simple document class
Bite 311. Cleaning text with pandas
Bite 312. Scoring objects
Bite 313. Alternative constructors
Bite 315. More logging practice
Bite 316. To rent or to stream movies?
Bite 320. sortable dataclasses and enums
Bite 325. Floating point arithmetic
Bite 326. Abstract Syntax Tree (AST) Printer
Bite 332. Searching for an apartment
Bite 334. Simple TCP client
Bite 335. Async HTTP client
Bite 338. Create food objects
Bite 339. Retrieve food objects
Bite 340. Update and delete food objects
Bite 341. Pydantic part II
Bite 342. Food logging CRUD
Bite 343. FastAPI Exception handling
Bite 344. Return an HTML response
Bite 348. Citation indexes
Bite 349. Writing better Spanish
Bite 351. Get spelling suggestions
Bite 352. Hash SQL statements
Bite 354. When to Use Command Line Option (CLI) Options and When CLI Arguments?
Bite 356. Using Typer Callbacks to Create Command Line Interface (CLI) Parameters
Bite 358. Implementation of a Simple Typer Test
Bite 361. Rich Excursion - Create Beautiful Tables
Bite 362. Add a Password Prompt to Your Command Line Interface (CLI)
Bite 363. Movie Theater (Refactoring)
Bite 364. Create Wikipedia Lorem Ipsum text
Bite 365. Rolling two dice for an advantage
Bite 366. Goal Tracker
Bite 367. Add Pi Day to the calendar
Bite 368. Hello Types
Bite 369. Advanced Type Hints
Bite 370. Getting started with vectors
Bite 374. Group Anagrams
Bite 375. Find All Letter Combinations of a Phone Number
Bite 377. Coins on the Table
Bite 2. Regex Fun
Bite 11. Enrich a class with dunder methods
Bite 20. Write a context manager
Bite 23. Find words that are > 95% similar
Bite 24. ABC's and class inheritance
Bite 31. Matrix multiplication / @ operator
Bite 34. Building a Karma app - implement the User class
Bite 40. Write a binary search algorithm
Bite 42. Number Guessing Game Class
Bite 50. Make a little PyBites search engine (feedparser)
Bite 52. Create a movie quote API with Flask
Bite 53. Convert text into multiple columns
Bite 58. Using argparse to interface with a grocery cart
Bite 61. Create a variable size Paw Patrol card deck with random actions
Bite 63. Use an infinite iterator to simulate a traffic light
Bite 69. Regex Fun - part II
Bite 75. Parse Unix cal to a weekday mapping
Bite 76. The singledispatch countdown challenge
Bite 85. Write a score property
Bite 88. Write a performance monitoring context manager
Bite 93. Rock-paper-scissors and generator's send
Bite 94. Parse PyCon talk data from YouTube
Bite 98. Code your way out of a grid
Bite 112. Social Media Username Validator
Bite 121. Determine the strength of a password
Bite 124. Marvel data analysis
Bite 126. The Emoji (Unicode) Bite
Bite 131. Screen scraper
Bite 134. Two Sums
Bite 139. Calculate a coding streak in days
Bite 145. Record Breakers
Bite 152. Manipulate string decorator
Bite 158. Subclass the list built-in
Bite 160. 15-way Rock Paper Scissors
Bite 164. CLI tool: HTML link converter (stdin to stdout)
Bite 168. Ninja Rankings
Bite 174. String manipulation and metrics
Bite 170. Analyze McDonald's food data
Bite 171. Make a terminal spinner animation
Bite 177. Use Pandas to find most common genres in a movie excel sheet
Bite 179. Strip comments from Python code
Bite 183. Analyze sales data with pandas
Bite 196. Create a JS-like dict object
Bite 198. Calculate my Mac's longest uptime
Bite 200. inecraft Enchantable Items
Bite 204. Pomodoro with asyncio
Bite 207. Cached property decorator
Bite 211. Write a retry decorator
Bite 213. Code a translation fixer
Bite 216. Parse an email header
Bite 220. Analysing @pythonbytes RSS feed
Bite 224. Get sentences from a text
Bite 229. Scrape best programming books
Bite 237. Get the dates Ninja belts were earned
Bite 240. Write tests for an Account class
Bite 242. Zodiacal data parsing
Bite 248. Test a number guessing game
Bite 249. Test a movie DB class
Bite 250. PyBites URL Shortener
Bite 260. Let's play with Pandas DataFrames
Bite 266. Composition, Inheritance, Abstract Base Class, what?
Bite 269. Taxable Income Calculator
Bite 268. Number Transformers
Bite 273. Shortest path (Graph Bite)
Bite 276. Get Father's days by date and country
Bite 277. Number of coin changes
Bite 280. Regular Expression Lookahead/Lookbehind
Bite 281. Generating sales reports from Github data
Bite 282. Evaluate a Bridge hand
Bite 292. Scoring matrices
Bite 294. Bowling score
Bite 297. Rename keys
Bite 300. 🥳 pto calculator
Bite 303. Unique genes
Bite 310. Create file pairs
Bite 321. Magic bytes
Bite 327. AST visitor
Bite 328. Longest coding streak
Bite 329. Convert dict keys to snake case
Bite 330. Simple Math Equation Solver
Bite 331. Convolution in Neural Networks
Bite 333. Metropolis–Hastings Algorithm
Bite 345. FastAPI Authentication with JWT (JSON Web Tokens)
Bite 350. Learn to handle cron schedule expressions
Bite 359. Implementation of a More Sophisticated Typer Tests
Bite 376. Art Thief
Bite 378. Organizational Chart
Bite 379. Hedge Maze
"""


def create_bite_map(bites):
    bites_map = {}
    for line in bites.splitlines():
        bite, description = line.split(".", 1)
        bite_num = bite.split()[1]
        bites_map[bite_num] = description.strip().capitalize()
    return bites_map


def fetch_bites_api():
    r = requests.get(BITES_API)
    with open("bites_api_data.json", "w") as f:
        json.dump(r.json(), f, indent=2)


def format_bites_api():
    with open("bites_api_data.json") as f:
        data = json.load(f)
    return {bite["title"]: bite for bite in data}


def create_description_list(bites):
    bite_descriptions = []
    for line in bites.splitlines():
        bite, description = line.split(".", 1)
        bite_descriptions.append(description)
    return bite_descriptions


def get_dirs() -> list[pathlib.Path]:
    dirs = [d for d in pathlib.Path(".").iterdir() if d.is_dir() and d.name.isdigit()]
    return dirs


def convert_dirs(bites_map: dict, formatted_bites: dict):
    dirs = get_dirs()
    if not dirs:
        print("No old bite dirs found")
        return
    local_bites = {}
    for d in dirs:
        old_dir = d.name
        if old_dir not in bites_map:
            continue
        bite_title = bites_map.get(old_dir)
        slug = formatted_bites[bite_title]["slug"]
        local_bites[bite_title] = f"{URL_BASE}{slug}/"
        try:
            pathlib.Path(old_dir).rename(pathlib.Path(slug))
        except FileExistsError:
            continue
        except OSError:
            print(f"Failed to rename {old_dir} to {slug}")
            continue
    with open(".local_bites.json", "w") as f:
        json.dump(local_bites, f, indent=2)


# def add_local_bites(bites_map):
#     dirs = [d for d in pathlib.Path(".").iterdir() if d.is_dir()]
#     local_bites = {}
#     for dir in dirs:
#         for description in create_description_list(BITES):
#             if slugify(description) == dir.name:
#                 local_bites[description.strip()] = URL_BASE + dir.name.replace("_", "-")
#                 break
#     with open(".local_bites.json", "w") as f:
#         json.dump(local_bites, f, indent=2)


if __name__ == "__main__":
    from rich import print

    bites_map = create_bite_map(BITES)
    formatted_bites = format_bites_api()

    convert_dirs(bites_map, formatted_bites)
    # add_local_bites(bites_map)
