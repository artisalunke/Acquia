.. include:: /common/global.rst

Using Markdown in tickets
=========================

When you create a new Acquia Support ticket, you must enter a `ticket description in the Description field </support/tickets#description>`__. Acquia's ticketing system allows you to use Markdown. Markdown is a lightweight text syntax that is easily converted into HTML, so you can write clearer, better-formatted descriptions.

You don't need to know anything about Markdown to write your description — you can just type plain text. Pressing the **Enter** key twice is enough to separate your text into paragraphs. But if you want to go further, you can format your description with a few simple characters:

.. list-table::
 :widths: 10 35 55
 :header-rows: 1

 * - Type
   - Formatting
   - Example
 * - Bulleted list
   - Put an asterisk ( ``*`` ), a plus sign ( ``+`` ), or a minus sign ( ``-`` ) followed by a space, in front of each line in the list.
   - ``* This`` |br| 
     ``* Is a`` |br| 
     ``* List``
     
     becomes:
   
     - This
     - Is a
     - List
 * -  Numbered list
   - Put a number, followed by a period, in front of each line in the list. It does not matter which numbers you use; Markdown will number them in order, starting with 1.
   - ``1. This`` |br| 
     ``1. Is a`` |br| 
     ``9. List``

     becomes
   
     #. This
     #. Is a
     #. List
 * - Headers
   - Put pound signs ( ``#`` ) at the head of the line. Each # increases the level of the header, so ## is an h2 header, and ### is an h3 header.
   - 
 * - Link
   - Use square brackets ( ``[ ]`` ) to delimit the text you want to turn into a link, followed by the link URL in parentheses ( ``( )`` ).
   - ``[here is a link](http://www.example.com)``
 * - Image
   - Use an exclamation mark ( ``!`` ) at the beginning of a line, followed by the alt text in square brackets ( ``[ ]`` ) and the image URL in parentheses ( ``( )`` ).
   - ``![Example logo](http://example.com/images/logo.png)``
 * - Code
   - Use a backtick ( ````` ) at the beginning and end of the code in a sentence. For code blocks, indent the entire block of code with four spaces.
   - ```This is inline code```

Additional resources
--------------------

That's not everything you can do with Markdown, but that should cover the most useful formatting options. For more information about Markdown, see the following resources:

-  `Markdown basics <https://daringfireball.net/projects/markdown/basics>`__
-  `Full syntax documentation <http://daringfireball.net/projects/markdown/syntax>`__
