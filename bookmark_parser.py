#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import ply

#<!DOCTYPE NETSCAPE-Bookmark-file-1>
#<!-- This is an automatically generated file.
     #It will be read and overwritten.
     #DO NOT EDIT! -->
#<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
#<TITLE>Bookmarks</TITLE>
#<H1>Bookmarks Menu</H1>

tokens = ("START_TAG", "START_END_TAG", "CLOSE_TAG", "CLOSE_END_TAG",
          "DT", "DL", "PARA", "ANCHOR", "HEADING",
          "HREF_ATTR", "ADD_ATTR", "MODIFIED_ATTR",
          "URI", "DOUBLE_QUOTE", "INTEGER",
          "DOCTYPE", "NETSCAPE_SPEC", "COMMENT_START", "COMMENT_END", "META",
          "TITLE", "H1", "GENERIC_TEXT",
          )

t_DT = 'DT'
t_DL = 'DL'
t_PARA = 'p'
t_ANCHOR = 'A'
t_HEADING = 'H3'
t_HREF_ATTR = 'HREF'
t_ADD_ATTR = 'ADD_DATE'
t_MODIFIED_ATTR = 'LAST_MODIFIED'
# see RFC3986, Appendix B
t_URI = r'^(([^:/?\#]+):)(//([^/?\#]*))([^?\#]*)(\?([^\#]*))?(\#(.*))?'
# but RFC6874 adds
# IP-literal = "[" ( IPv6address / IPv6addrz / IPvFuture  ) "]"
# ZoneID = 1*( unreserved / pct-encoded )
# IPv6addrz = IPv6address "%25" ZoneID
t_DOUBLE_QUOTE = '"'
t_INTEGER = r'[0-9]+'
t_DOCTYPE = r'!DOCTYPE'
t_NETSCAPE_SPEC = 'NETSCAPE-Bookmark-file-1'
t_META = '<META [^>]+>'
t_TITLE = '<TITLE>.+</TITLE>'
t_H1 = '<H1>.+</H1>'
t_COMMENT_START = '!--'
t_COMMENT_END = '-->'
t_START_TAG = r'<'
t_START_END_TAG = r'</'
t_CLOSE_TAG = r'>'
t_CLOSE_END_TAG = r'/>'

# damn. after COMMENT_START we need to switch modes, just consume everything until -->

#precedence = (
     #("nonassoc", "DOCTYPE", ),
     #("right", "START_TAG", ),
#)

t_ignore = " \t"

def t_error(t):
     print("Illegal character '{}'".format(t.value[0]))
     t.lexer.skip(len(t.value))

def t_newline(t):
     r'\n+'
     t.lexer.lineno += t.value.count("\n")

import ply.lex as lex

try:
     lexer = lex.lex()
except SyntaxError as e:
     sys.stderr.write("Failed to build lexer\n")
     sys.stderr.write(str(e))
     sys.stderr.write('\n')

     sys.exit(1)

def p_document(t):
     'document : doctype_tag comment META TITLE H1 start_dl'
     pass

def p_start_dl(t):
     'start_dl : START_TAG DL CLOSE_TAG'
     pass

def p_end_dl(t):
     'end_dl : START_END_TAG DL CLOSE_TAG'
     pass

def p_doctype_tag(t):
     'doctype_tag : START_TAG DOCTYPE NETSCAPE_SPEC CLOSE_TAG'
     pass

def p_comment(t):
     'comment : START_TAG COMMENT_START GENERIC_TEXT COMMENT_END'
     pass

def p_error(t):
     if t:
          print("Syntax error at '{}'".format(t.value))
          print(t)
     else:
          print("Syntax error")

import ply.yacc as yacc
try:
     parser = yacc.yacc()
except ply.yacc.YaccError as e:
     sys.stderr.write("Failed to build parser\n")
     sys.stderr.write(str(e))
     sys.stderr.write('\n')

     sys.exit(2)


with open('data/bookmarks_part.html', 'r') as htmlin:
     s = htmlin.read()

parser.parse(s, lexer=lexer, debug=True, tracking=True)
