Title: Markdown Styling Test
url:
save_as: test.html

----

[TOC]

# Font test

```.java
/*
10
1234567890
20
12345678901234567890
30
123456789012345678901234567890
40
1234567890123456789012345678901234567890
50
12345678901234567890123456789012345678901234567890
60
123456789012345678901234567890123456789012345678901234567890
70
1234567890123456789012345678901234567890123456789012345678901234567890
80
12345678901234567890123456789012345678901234567890123456789012345678901234567890
90
123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
100
1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890

// Following by " write some example java code. This is to test syntax highlighting, so try to use every syntactical element. However, it doesn't need to actually compile or work.", Gemini 2.5 Pro, Google, 2025-09-19, https://gemini.google.com/app
/*
 * Javadoc Comment:
 * This is a demonstration file for syntax highlighting in Java.
 * It includes a variety of language features.
 * @author Gemini
 * @version 1.0
 */
package com.example.syntax;

// Import statements
import java.util.ArrayList;
import java.util.List;
import java.util.function.Consumer;
import static java.lang.Math.PI;

/**
 * An abstract class to demonstrate various Java syntax elements.
 * It implements a generic interface.
 * @param <T> The generic type parameter.
 */
@Deprecated
public abstract class SyntaxHighlightingDemo<T extends Number> implements Runnable {

    // Fields with different modifiers
    public static final String CONSTANT_STRING = "Hello, World!";
    private int privateIntField = 0b101010; // Binary literal
    protected double protectedDoubleField = 1.23e4; // Scientific notation
    volatile boolean isRunning = true;
    transient long transientLongField = 123_456_789L; // Underscores in literals
    char hexChar = '\u0041'; // Unicode escape

    // Static initializer block
    static {
        System.out.println("Static block initialized.");
    }

    // Instance initializer block
    {
        this.privateIntField = 42;
    }

    // Constructor
    public SyntaxHighlightingDemo(int initialValue) {
        this.privateIntField = initialValue;
    }

    // Abstract method
    public abstract void performAction(T input);

    // Final method
    public final synchronized void start() {
        if (!isRunning) {
            this.isRunning = true;
            new Thread(this).start();
        }
    }

    // Generic method with throws clause
    @SuppressWarnings("unchecked")
    public <E> E genericMethod(List<?> list) throws IllegalArgumentException {
        if (list == null || list.isEmpty()) {
            throw new IllegalArgumentException("List cannot be empty");
        }
        return (E) list.get(0);
    }

    // Method with various control flow statements
    @Override
    public void run() {
        // A multi-line comment section
        /*
         * This loop demonstrates labels, continue, and break.
         */
        outerLoop:
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (i * j > 50) {
                    System.out.println("Breaking outer loop");
                    break outerLoop;
                }
                if (j % 2 == 0) {
                    continue;
                }
            }
        }

        // Try-catch-finally block
        try {
            int result = 10 / privateIntField;
            System.out.println(result);
        } catch (ArithmeticException e) {
            System.err.println("Caught an exception: " + e.getMessage());
        } finally {
            System.out.println("Finally block executed.");
        }

        // Switch statement with a record pattern (preview feature)
        Object obj = "Test";
        switch (obj) {
            case String s -> System.out.println("It's a string: " + s);
            case Integer i -> System.out.println("It's an integer: " + i);
            default -> System.out.println("Something else.");
        }
        
        // Lambda expression and method reference
        List<String> names = new ArrayList<>(List.of("Alice", "Bob"));
        names.forEach(s -> System.out.println(s.toUpperCase()));
        names.forEach(System.out::println);
    }

    // Native method declaration
    public native long getSystemTime();

    // Inner class
    private class InnerHelper {
        void help() {
            // Accessing outer class field
            System.out.println(SyntaxHighlightingDemo.this.privateIntField);
        }
    }

    // Static nested class
    public static class StaticNested {
        public static void utilityMethod() {
            double circleArea = PI * 2 * 2;
        }
    }
}

// Interface with default and static methods
interface Actionable {
    void doSomething();

    default void doDefault() {
        System.out.println("Default implementation.");
    }

    static void staticInterfaceMethod() {
        System.out.println("Static method in an interface.");
    }
}

// Enum definition
enum Color {
    RED("#FF0000"), GREEN("#00FF00"), BLUE("#0000FF");

    private final String hexCode;

    Color(String code) {
        this.hexCode = code;
    }

    public String getHexCode() {
        return hexCode;
    }
}

// Annotation definition
@interface MyAnnotation {
    String value();
    int version() default 1;
}

// Record class - a modern Java feature
record Point(int x, int y) {}

// Sealed class hierarchy - another modern feature
sealed class Shape permits Circle, Square {
    // A class that can only be extended by specific classes
}

final class Circle extends Shape {
    float radius;
}

non-sealed class Square extends Shape {
    float side;
}
*/
```

# Citation

<cite>"markdown-test-file", mxstbr, Max Stoiber, https://github.com/mxstbr/markdown-test-file, 2025-09-19</cite>

# Markdown: Syntax

## Overview

### Philosophy

Markdown is intended to be as easy-to-read and easy-to-write as is feasible.

Readability, however, is emphasized above all else. A Markdown-formatted
document should be publishable as-is, as plain text, without looking
like it's been marked up with tags or formatting instructions. While
Markdown's syntax has been influenced by several existing text-to-HTML
filters -- including [Setext](http://docutils.sourceforge.net/mirror/setext.html), [atx](http://www.aaronsw.com/2002/atx/), [Textile](http://textism.com/tools/textile/), [reStructuredText](http://docutils.sourceforge.net/rst.html),
[Grutatext](http://www.triptico.com/software/grutatxt.html), and [EtText](http://ettext.taint.org/doc/) -- the single biggest source of
inspiration for Markdown's syntax is the format of plain text email.

## Block Elements

### Paragraphs and Line Breaks

A paragraph is simply one or more consecutive lines of text, separated
by one or more blank lines. (A blank line is any line that looks like a
blank line -- a line containing nothing but spaces or tabs is considered
blank.) Normal paragraphs should not be indented with spaces or tabs.

The implication of the "one or more consecutive lines of text" rule is
that Markdown supports "hard-wrapped" text paragraphs. This differs
significantly from most other text-to-HTML formatters (including Movable
Type's "Convert Line Breaks" option) which translate every line break
character in a paragraph into a `<br />` tag.

When you *do* want to insert a `<br />` break tag using Markdown, you
end a line with two or more spaces, then type return.

### Headers

Markdown supports two styles of headers, [Setext] [1] and [atx] [2].

Optionally, you may "close" atx-style headers. This is purely
cosmetic -- you can use this if you think it looks better. The
closing hashes don't even need to match the number of hashes
used to open the header. (The number of opening hashes
determines the header level.)


### Blockquotes

Markdown uses email-style `>` characters for blockquoting. If you're
familiar with quoting passages of text in an email message, then you
know how to create a blockquote in Markdown. It looks best if you hard
wrap the text and put a `>` before every line:

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
> 
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.

Markdown allows you to be lazy and only put the `>` before the first
line of a hard-wrapped paragraph:

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.

Blockquotes can be nested (i.e. a blockquote-in-a-blockquote) by
adding additional levels of `>`:

> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.

Blockquotes can contain other Markdown elements, including headers, lists,
and code blocks:

> ## This is a header.
> 
> 1.   This is the first list item.
> 2.   This is the second list item.
> 
> Here's some example code:
> 
>     return shell_exec("echo $input | $markdown_script");

Any decent text editor should make email-style quoting easy. For
example, with BBEdit, you can make a selection and choose Increase
Quote Level from the Text menu.


### Lists

Markdown supports ordered (numbered) and unordered (bulleted) lists.

Unordered lists use asterisks, pluses, and hyphens -- interchangably
-- as list markers:

*   Red
*   Green
*   Blue

is equivalent to:

+   Red
+   Green
+   Blue

and:

-   Red
-   Green
-   Blue

Ordered lists use numbers followed by periods:

1.  Bird
2.  McHale
3.  Parish

It's important to note that the actual numbers you use to mark the
list have no effect on the HTML output Markdown produces. The HTML
Markdown produces from the above list is:

If you instead wrote the list in Markdown like this:

1.  Bird
1.  McHale
1.  Parish

or even:

3. Bird
1. McHale
8. Parish

you'd get the exact same HTML output. The point is, if you want to,
you can use ordinal numbers in your ordered Markdown lists, so that
the numbers in your source match the numbers in your published HTML.
But if you want to be lazy, you don't have to.

To make lists look nice, you can wrap items with hanging indents:

*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.

But if you want to be lazy, you don't have to:

*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
Suspendisse id sem consectetuer libero luctus adipiscing.

List items may consist of multiple paragraphs. Each subsequent
paragraph in a list item must be indented by either 4 spaces
or one tab:

1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.

It looks nice if you indent every line of the subsequent
paragraphs, but here again, Markdown will allow you to be
lazy:

*   This is a list item with two paragraphs.

    This is the second paragraph in the list item. You're
only required to indent the first line. Lorem ipsum dolor
sit amet, consectetuer adipiscing elit.

*   Another item in the same list.

To put a blockquote within a list item, the blockquote's `>`
delimiters need to be indented:

*   A list item with a blockquote:

    > This is a blockquote
    > inside a list item.

To put a code block within a list item, the code block needs
to be indented *twice* -- 8 spaces or two tabs:

*   A list item with a code block:

        <code goes here>

### Code Blocks

Pre-formatted code blocks are used for writing about programming or
markup source code. Rather than forming normal paragraphs, the lines
of a code block are interpreted literally. Markdown wraps a code block
in both `<pre>` and `<code>` tags.

To produce a code block in Markdown, simply indent every line of the
block by at least 4 spaces or 1 tab.

This is a normal paragraph:

    This is a code block.

Here is an example of AppleScript:

    tell application "Foo"
        beep
    end tell

A code block continues until it reaches a line that is not indented
(or the end of the article).

Within a code block, ampersands (`&`) and angle brackets (`<` and `>`)
are automatically converted into HTML entities. This makes it very
easy to include example HTML source code using Markdown -- just paste
it and indent it, and Markdown will handle the hassle of encoding the
ampersands and angle brackets. For example, this:

    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

Regular Markdown syntax is not processed within code blocks. E.g.,
asterisks are just literal asterisks within a code block. This means
it's also easy to use Markdown to write about Markdown's own syntax.

```
tell application "Foo"
    beep
end tell
```

## Span Elements

### Links

Markdown supports two style of links: *inline* and *reference*.

In both styles, the link text is delimited by [square brackets].

To create an inline link, use a set of regular parentheses immediately
after the link text's closing square bracket. Inside the parentheses,
put the URL where you want the link to point, along with an *optional*
title for the link, surrounded in quotes. For example:

This is [an example](http://example.com/) inline link.

[This link](http://example.net/) has no title attribute.

### Emphasis

Markdown treats asterisks (`*`) and underscores (`_`) as indicators of
emphasis. Text wrapped with one `*` or `_` will be wrapped with an
HTML `<em>` tag; double `*`'s or `_`'s will be wrapped with an HTML
`<strong>` tag. E.g., this input:

*single asterisks*

_single underscores_

**double asterisks**

__double underscores__

### Code

To indicate a span of code, wrap it with backtick quotes (`` ` ``).
Unlike a pre-formatted code block, a code span indicates code within a
normal paragraph. For example:

Use the `printf()` function.
