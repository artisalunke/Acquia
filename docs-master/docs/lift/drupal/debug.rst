.. include:: /common/global.rst

Displaying |acquia-product:cha| diagnostic messages
===================================================

Because you're seamlessly integrating personalized content into your
website, it can be difficult to determine where errors and issues may be
occurring. Is it a theming issue with your website, or is
|acquia-product:cha| not serving the content that you expect?

To provide more insight into how |acquia-product:alt| is working with
your website, you can enable debug mode and view status and error
messages from |acquia-product:cha| in your browser's console window.

.. _enable:

Enabling debug mode
-------------------

To enable debug mode for |acquia-product:alt|, complete the following
steps:

#. Sign in to your website as a user with the `permission to administer
   the personalization settings </lift/drupal/install/enable>`__.
#. In the admin menu, go to **Configuration > Personalization
   settings**, and then click the **General** tab.
#. Select the **Debug mode** check box.
#. Click **Save configuration**.

|acquia-product:cha| debug messages will now start to appear in the
browser console of users configured to receive the messages.

.. _view:

Viewing messages in the browser console
---------------------------------------

By default, user accounts with the blank website permission can view
|acquia-product:cha| status messages in their browser console.

For more information about how to start the developer tools for your
browser, which includes the console for webpage status messages, see
`Browser developer tools </resource/browser-tool>`__.

Viewing messages for non-administrators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to view status messages for users who are not administrators
(including anonymous website visitors who have not signed in), you can
enable a browser cookie that enables the display of debug messages for
the browser.

Create a local cookie for the user called ``personalizeDebugMode`` with
a value of ``1``. After you save the cookie and reload the webpage,
|acquia-product:cha| status messages should appear in the browser's
console.

.. _list:

Diagnostic message listing
--------------------------

OK messages
~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Code                  | Message               | Description           |
+=======================+=======================+=======================+
| 2000                  | Decision being        | The personalization   |
|                       | requested from the    | code requested a      |
|                       | agent                 | personalized          |
|                       |                       | variation from the    |
|                       |                       | decision engine,      |
|                       |                       | which includes        |
|                       |                       | [acquia-products:cha] |
|                       |                       | .                     |
+-----------------------+-----------------------+-----------------------+
| 2001                  | Decision being read   | The personalization   |
|                       | from storage (cached  | code requested a      |
|                       | decision)             | personalized          |
|                       |                       | variation previously  |
|                       |                       | stored in the browser |
|                       |                       | cache.                |
+-----------------------+-----------------------+-----------------------+
| 2002                  | Showing pre-selected  | The personalization   |
|                       | option (option        | code requested a      |
|                       | preview or shareable  | personalized          |
|                       | option)               | variation based on a  |
|                       |                       | defined URL, which    |
|                       |                       | occurs when           |
|                       |                       | administrators select |
|                       |                       | a variation for       |
|                       |                       | preview, or if        |
|                       |                       | website visitors view |
|                       |                       | a particular          |
|                       |                       | variation from a      |
|                       |                       | shared link.          |
|                       |                       | To enable or disable  |
|                       |                       | shareable             |
|                       |                       | personalized          |
|                       |                       | variations for a      |
|                       |                       | personalization, edit |
|                       |                       | the personalization,  |
|                       |                       | select the variation  |
|                       |                       | set, and then in the  |
|                       |                       | **Advanced** section, |
|                       |                       | either select or      |
|                       |                       | clear the             |
|                       |                       | **Shareable** check   |
|                       |                       | box, respectively.    |
+-----------------------+-----------------------+-----------------------+
| 2003                  | Showing fallback      | The personalization   |
|                       | option (either due to | code requested the    |
|                       | admin mode or the     | default, fallback     |
|                       | campaign not active)  | variation for the     |
|                       |                       | variation set.        |
+-----------------------+-----------------------+-----------------------+
| 2020                  | Executor being called | The personalization   |
|                       | for decision          | engine displayed the  |
|                       |                       | requested             |
|                       |                       | personalized          |
|                       |                       | variation.            |
+-----------------------+-----------------------+-----------------------+

WARNING messages
~~~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Code                  | Message               | Description           |
+=======================+=======================+=======================+
| 3001                  | Client-side goal      | The personalization   |
|                       | registered to page    | code encountered a    |
|                       | but there’s no        | goal that does not    |
|                       | element matching      | match any of the      |
|                       |                       | displayed webpage's   |
|                       |                       | elements.             |
+-----------------------+-----------------------+-----------------------+
| 3002                  | Option set on the     | The personalization   |
|                       | page with selector    | code encountered a    |
|                       | that doesn’t match    | variation that does   |
|                       | any DOM element       | not match any of the  |
|                       |                       | elements in the       |
|                       |                       | webpage's document    |
|                       |                       | object model (DOM).   |
+-----------------------+-----------------------+-----------------------+

ERROR messages
~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Code                  | Message               | Description           |
+=======================+=======================+=======================+
| 5100                  | Problem getting a     | Your website could    |
|                       | decision from Lift    | not connect to        |
|                       |                       | |acquia-product:cha|. |
|                       |                       | Go to **Configuration |
|                       |                       | > Personalization     |
|                       |                       | settings > Acquia     |
|                       |                       | Lift**, and then      |
|                       |                       | click **Test          |
|                       |                       | connection to Acquia  |
|                       |                       | Lift** to test your   |
|                       |                       | connection.           |
|                       |                       | The personalization   |
|                       |                       | code instead          |
|                       |                       | requested the         |
|                       |                       | default, fallback     |
|                       |                       | variation for the     |
|                       |                       | variation set.        |
+-----------------------+-----------------------+-----------------------+
