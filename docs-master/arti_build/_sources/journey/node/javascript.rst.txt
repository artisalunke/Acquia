.. include:: /common/global.rst

JavaScript node
===============

|JavaScript node|

The JavaScript node executes any valid
`JavaScript <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference>`__
code as a function and can return any valid JavaScript object as a
return value. The function can also update any of its arguments by
reference, including public variables. The JavaScript Node supports
`Node 6 <https://nodejs.org/en/blog/release/v6.0.0/>`__, which is
ECMAScript (ES5) with 93% support for ECMAScript 2015 (ES6) features.

|acquia-product:aj| uses the `Node
JavaScript <https://nodejs.org/en/>`__ engine to execute the JavaScript
functions. The full `Node library <https://nodejs.org/api/>`__ is
available with a few notable exceptions for security reasons which
includes the ``http``, ``os`` and ``fs`` modules. Any valid Node
JavaScript can be executed within the function, including other embedded
functions. The Script Editor uses JavaScript syntax highlighting to help
ensure that the code is correct.

As well as the full node library the JavaScript node provides includes a
number of common packages that support common tasks:

-  Date and time manipulation (`moment <https://momentjs.com/>`__)
-  User agent parsing and device detection
   (`ua-parser-js <https://www.npmjs.com/package/ua-parser-js>`__)
-  ID generation (`uuid <https://www.npmjs.com/package/uuid>`__)
-  Toolkit for working with common data structures
   (`lodash <https://lodash.com/>`__)

See the `Examples <#examples>`__ section for suggestions on some of the
things that you can do with each of these packages.

.. note::
  JavaScript has `reserved
  words <http://www.w3schools.com/js/js_reserved.asp>`__ which cannot be
  used as variables, labels or function names.

Creating a JavaScript node
--------------------------

To create a conditional node, perform the following actions:

#. Sign in to your |acquia-product:aj| interface.
#. Identify the project you wish to modify.
#. Click the **Project Editor** |Project Editor icon| icon.
#. In the top left-hand corner of the screen, click the **Action Menu**
   |Action Menu icon| icon.
#. Select **+ Create New** from the list.
#. Enter the name of your new JavaScript node in the **Name** field.
#. Scroll through the list of node types to find the **Logic** section,
   and click **JavaScript**:
   |Logic node type listing|
#. Click **Create New Item**.
#. Paste in your desired Javascript function into the **JavaScript
   Editor**.
#. Click **Save Script**.

Adding arguments to a JavaScript node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When creating a JavaScript node, additional function arguments may be
added by clicking **Add Argument** in the top left-hand corner of the
**JavaScript Editor**, provide an argument name, and click **Save**.
Once an argument is added, you can update or delete an argument by
right-clicking on the argument name:

|Select an argument to edit|

For example, the following function will return the concatenation of two
arguments:

|JavaScript node example|

.. admonition:: Notes

  -  When deleting an argument, |acquia-product:aj| will not prompt you
     for confirmation.
  -  Arguments cannot be reordered. To work around this limitation, rename
     the arguments instead.

Any changes made to the input arguments will be reflected in the schema
(or public variable) after the function has run.

The JavaScript node is often used to set or change many schema values at
once. It can also be used as an alternative to a series of `Set
nodes </journey/node/set>`__ by setting all of the values in a single
node. For example, the function below will create a complex JavaScript
object that can be mapped into the schema or a public variable:

|More complex JavaScript example|

All of the Node JavaScript libraries are available with the exception of
the ``http``, ``fs`` and other libraries for security reasons. This
example uses the **Node Math** library to access the value of PI.

``function circleArea(r) {     // Returns the area of a circle given the radius - r     const PI = Math.PI;     return  PI * r * r; }``

Validation warnings
-------------------

There are no validation warnings created by the JavaScript node.

Testing
-------

When testing a JavaScript node the testing console allows the
specification of data for each of the arguments to the function. This
should be provided as valid input in JavaScript Object Notation (JSON)
for each of the arguments. Ignore the Data element on the left of the
testing window as that is not currently used.

For example testing the JavaScript node above that returns the two
arguments concatenated or added (depending on the type) together when
called with two strings:

|Testing settings|

will return as follows:

|Javascript node testing results|

However, that function will also work with numeric values:

|Javascript node testing with numeric values|

|Javascript node testing, numeric results|

Advanced Testing
----------------

If your JavaScript node is more complicated, then you will need to
ensure that each argument is given the correct JavaScript object. This
example displays a more complex version of the JavaScript node:

|Complex JavaScript node|

called with these parameters:

|javascript complex parameters|

It will produce this output:

|Complex result|

Return Value
------------

The return value from the JavaScript Node is only ever ``true`` or
``false`` — it does not return the actual return value of the function
from the ``return`` statement. This can sometimes be confusing and means
that it is not possible to branch directly from the result of the
JavaScript node on any values that are not ``true``, ``false``, or
``error``. You must use a `Get node </journey/node/get>`__ to get a
value to branch on within the graph.

In this example, the graph will only go to the JavaScript error branch
if the JavaScript throws an error.

|Javascript node erroring|

Examples
--------

The JavaScript node includes some common packages. The examples below
show how to use these functions in your own JavaScript nodes.

UUID
~~~~

The `UUID package <https://www.npmjs.com/package/uuid>`__ is used to
generate unique identifiers of various different types.

``// Generate a v1 UUID (time-based) const uuidV1 = require('uuid/v1'); uuidV1(); // -> '6c84fb90-12c4-11e1-840d-7b25c5ee775a'  // Generate a v4 UUID (random) const uuidV4 = require('uuid/v4'); uuidV4(); // -> '110ec58a-a0f2-4ac4-8393-c866d813b8d1'``

Moment
~~~~~~

This `moment package <https://momentjs.com/>`__ is used to parse,
validate, manipulate, and display dates and times in JavaScript.

.. note::
  |acquia-product:aj| supports moment.js version 2.18.1

Sample moment code

``const moment = require ('moment'); const obj = {};   obj.curTime1 = moment().format('MMMM Do YYYY, h:mm:ss a'); obj.curTime2 = moment().format('dddd'); obj.curTime3 = moment().format("MMM Do YY"); obj.curTime4 = moment().format('YYYY [escaped] YYYY'); obj.curTime5 = moment().format();   return obj;``

Some of the most common use cases for date manipulation in
|acquia-product:aj| are for calculating the difference in days between
two dates and also calculating a new date by adding (or subtracting)
from a given date.

This ``diffDays JavaScript function`` is the code for calculating the
difference in days, positive or negative, between two dates which are
passed as strings:

``const moment = require('moment') // This function requires two dates to be passed as valid strings that the moment package will parse // See https://momentjs.com/docs/ for more information var dt1 = moment(d1) if (!dt1.isValid()) return 'd1 is not a valid date' var dt2 = moment(d2) if (!dt2.isValid()) return 'd2 is not a valid date'   // Will return positive and negative values return dt1.diff(dt2,'days')``

and in the javaScript Node:

|diffdays script|

The code to add a number of days to a specific date is very simple and
to return that date as a string:

``const moment = require('moment') // This function requires a date passed as valid string and a number of days to be added // See https://momentjs.com/docs/ for more information var dt1 = moment(d1) if (!dt1.isValid()) return 'd1 is not a valid date'   return moment(dt1).add(parseInt(days), 'days').format('YYYY-MM-DD')``

and in the JavaScript Node:

|addDays script|

ua-parser-js
~~~~~~~~~~~~

This library to detect browser, layout engine, operating system, CPU
architecture, and device type/model, entirely from user-agent string.

``user agent parser script const UAParser = require('ua-parser-js') // This function parses the User Agent String returned from a browser - typically via web tracking and returns an object that has details // on browser, operating system and device if it is not a desktop browser const parser = new UAParser(uaString) return parser.getResult();``

will return a JavaScript object that can be added to the schema like
this:

``{     "engine": {         "version": "537.36",         "name": "WebKit"     },     "os": {         "version": "10.12.4",         "name": "Mac OS"     },     "device": {},     "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",     "cpu": {},     "browser": {         "major": "58",         "version": "58.0.3029.110",         "name": "Chrome"     } }``

lodash
~~~~~~

Pronounced "LO-DASH", a modern JavaScript utility library delivering
modularity, performance and extras. Any functions in
`lodash.com/docs/4.17.4 <https://lodash.com/docs/4.17.4>`__ can be used
for ``array``, ``string``, ``lang``, ``math``, ``number``, and
``object`` manipulation.

.. note::
  |acquia-product:aj| Lodash version 4.17.4.

.. |JavaScript node| image:: https://cdn2.webdamdb.com/1280_s1lM0x6aVl57.png?1526475692
   :class: no-sb float-left logo-sm-lift
   :width: 51px
.. |Project Editor icon| image:: https://cdn4.webdamdb.com/100th_sm_YcVG2zY8pZL5.png?1526475783
   :width: 33px
   :height: 29px
.. |Action Menu icon| image:: https://cdn3.webdamdb.com/100th_sm_Aa8wvVef08x7.png?1526475662
   :width: 26px
   :height: 22px
.. |Logic node type listing| image:: https://cdn3.webdamdb.com/1280_kfNiX7lNWL28.png?1526475881
   :width: 377px
   :height: 116px
.. |Select an argument to edit| image:: https://cdn4.webdamdb.com/1280_kJLwZno2Va25.jpg?1526475824
   :width: 387px
   :height: 133px
.. |JavaScript node example| image:: https://cdn3.webdamdb.com/1280_gn8DuaudRB66.png?1526476155
   :width: 468px
   :height: 104px
.. |More complex JavaScript example| image:: https://cdn4.webdamdb.com/1280_w3UvcPuNNfY7.png?1526475685
   :width: 548px
   :height: 341px
.. |Testing settings| image:: https://cdn3.webdamdb.com/1280_kDxuHPB54WT8.png?1526475601
   :width: 747px
   :height: 472px
.. |Javascript node testing results| image:: https://cdn4.webdamdb.com/1280_QVtFDs68MDj0.png?1526475650
   :width: 617px
   :height: 476px
.. |Javascript node testing with numeric values| image:: https://cdn2.webdamdb.com/1280_kjjeZ3fhOch4.png?1526475812
   :width: 745px
   :height: 470px
.. |Javascript node testing, numeric results| image:: https://cdn4.webdamdb.com/1280_cFaGJ1lmykz0.png?1526476086
   :width: 622px
   :height: 478px
.. |Complex JavaScript node| image:: https://cdn3.webdamdb.com/1280_IxNwvZW3j321.png?1526476057
   :width: 559px
   :height: 203px
.. |javascript complex parameters| image:: https://cdn2.webdamdb.com/1280_EOIWiErbh6c0.png?1526475856
   :width: 550px
   :height: 345px
.. |Complex result| image:: https://cdn4.webdamdb.com/1280_IuIFxvzOs4X4.png?1526475950
   :width: 477px
   :height: 166px
.. |Javascript node erroring| image:: https://cdn3.webdamdb.com/1280_61M5Og582xq8.png?1526476113
   :width: 739px
   :height: 381px
.. |diffdays script| image:: https://cdn2.webdamdb.com/1280_VStGZKb3tO36.png?1526475442
   :width: 600px
   :height: 199px
.. |addDays script| image:: https://cdn2.webdamdb.com/1280_MReREPi0ceL9.png?1526476149
   :width: 600px
   :height: 183px
