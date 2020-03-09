import os, strformat, system

type
  TokenKind = enum
    META_IDENTIFIER,
    IDENTIFIER,
    COLON,
    NEWLINE,
    INDENT,
    OUTDENT,
    EOF

  Token = object
    line: int
    case kind: TokenKind
    of META_IDENTIFIER: mstr: string
    of IDENTIFIER: istr: string
    of COLON: nil
    of NEWLINE: nil
    of INDENT: nil
    of OUTDENT: nil
    of EOF: nil

  Scanner = ref object
    source: string
    hadError: bool
    tokens: seq[Token]
    start: int
    current: int
    line: int


proc report(line: int, where: string, message: string) =
  echo fmt"[line {line}] Error{where}: {message}"

proc error*(scanner: Scanner, line: int, message: string) =
  report(line, "", message)
  scanner.hadError = true


proc isAtEnd(scanner: Scanner): bool =
  return scanner.current >= scanner.source.len


proc advance(scanner: Scanner): char =
  scanner.current += 1
  return scanner.source[scanner.current - 1]


proc scanToken(scanner: Scanner): void =
  var c: char = scanner.advance()
  case c
    of ':': scanner.tokens.add(Token(kind: COLON))
    of '\n':
      scanner.tokens.add(Token(kind: NEWLINE))
      scanner.line += 1
    else: discard

proc scanTokens(scanner: Scanner): void =
  while not scanner.isAtEnd():
    scanner.start = scanner.current
    scanner.scanToken()

  scanner.tokens.add(Token(kind: EOF, line: scanner.line))


proc newScanner(source: string): Scanner =
  result = Scanner(
    source: source,
    hadError: false,
    tokens: @[],
    start: 0,
    current: 0,
    line: 1,
  )
  result.scanTokens()


proc main() =
  if paramCount() == 1:
    let source = readFile(paramStr(1))
    let scanner = newScanner(source)
    if scanner.hadError:
      quit(1)
    else:
      for token in scanner.tokens:
        echo fmt"Token: {token}"
  else:
    echo "Usage: cardman sample.card"


if isMainModule:
  main()
