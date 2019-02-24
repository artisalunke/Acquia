.. include:: /common/global.rst

R Model node
============

|R Script node|

The R Model node allows arbitrary `R
Language <https://www.r-project.org/>`__ scripts to be executed as part
of a graph.

The R node allows functions to be defined which can be passed optional
arguments. The return value of the function is the value of the last
expression in the function.

|R Node example|

All arguments are passed as strings and so type conversions are
necessary before manipulation as numeric values for example. The example
function below returns the sum of the two numeric input arguments.

|R Node code|

In a graph it is necessary to map the input arguments and the return
value from the function. Here the schema is being used to map the values
for the arguments above:

|R Node testing|

Resulting in the expected sum:

|R Node sum|

Vector arguments and return values
----------------------------------

A vector can be represented in JSON as a string field with separators.
This example shows how a string field using a comma as a separator can
be used as an input value and transformed into an R vector of numeric
values.

|R Node comma separated|

Similarly return vectors can be transformed into separated string fields
using the ``paste()`` function:

|R Node paste function|

Creating an R node
------------------

To create an R node, perform the following actions:

#. Sign in to your |acquia-product:aj| interface.
#. Identify the project you wish to modify.
#. Click the **Project Editor** |Project Editor icon| icon.
#. In the top left-hand corner of the screen, click the **Action Menu**
   |Action Menu icon| icon.
#. Select **+ Create New** from the list.
#. Enter the name of your new R node in the **Name** field.
#. Scroll through the list of node types to find the **Logic** section,
   and click **R Script**:
   |Logic node type listing|
#. Click **Create New Item**.

.. |R Script node| image:: https://cdn2.webdamdb.com/1280_gW4YuksHsEf0.png?1526475452
   :class: no-sb float-left logo-sm-lift
   :width: 51px
.. |R Node example| image:: https://cdn4.webdamdb.com/1280_oiAwqWpzmV31.png?1526476036
   :width: 597px
   :height: 183px
.. |R Node code| image:: https://cdn2.webdamdb.com/1280_U1En8mmMBv02.png?1526475477
   :width: 570px
   :height: 200px
.. |R Node testing| image:: https://cdn3.webdamdb.com/1280_QS8zaPZJYUm7.png?1526475496
   :width: 599px
   :height: 281px
.. |R Node sum| image:: https://cdn4.webdamdb.com/1280_kExN7c4Yie82.png?1526475867
   :width: 201px
   :height: 102px
.. |R Node comma separated| image:: https://cdn3.webdamdb.com/1280_AH1hNH7GiAX9.png?1526476016
   :width: 506px
   :height: 207px
.. |R Node paste function| image:: https://cdn4.webdamdb.com/1280_E589mDZQXrc8.png?1526475859
   :width: 503px
   :height: 202px
.. |Project Editor icon| image:: https://cdn4.webdamdb.com/100th_sm_YcVG2zY8pZL5.png?1526475783
   :width: 33px
   :height: 29px
.. |Action Menu icon| image:: https://cdn3.webdamdb.com/100th_sm_Aa8wvVef08x7.png?1526475662
   :width: 26px
   :height: 22px
.. |Logic node type listing| image:: https://cdn3.webdamdb.com/1280_kfNiX7lNWL28.png?1526475881
   :width: 377px
   :height: 116px
