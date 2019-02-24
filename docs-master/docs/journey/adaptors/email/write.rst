.. include:: /common/global.rst

Email: Write adaptor
====================

The write adaptor for emails sends an HTML email through an `email
connection </journey/connect/email>`__. The email **Message Body** and
**Subject** can be parameterized using any data elements, and the **To**
and **From** fields can be specified by any data element.

Creating the adaptor
--------------------

To use the email adaptor, complete the following steps:

#. `Create an adaptor </journey/adaptors>`__ of the type **Email**.
#. Configure the following settings for the adaptor:

   -  **To** - In the **Data Schema** panel, find the schema location
      that is the source for the email recipient, click its name, and
      then click the left arrow icon |left arrow| to set the **To**
      field to that location — you can also use a `literal
      value </journey/data#literal>`__
   -  **From** - Perform the same action as for the `**To**
      field <#to>`__
   -  **Subject** - Enter a concise topic for the email
   -  **Message Body** - Enter the contents of the email message

#. *Optional* - If you need to set an address for carbon copy (CC),
   blind carbon copy (BCC), or Reply-to, click **Optional Fields**, and
   then complete the procedure for the `**To** field <#to>`__ to
   populate each field as necessary from the **Data Schema**.
#. After you have completed your changes, click **Save Subject & Message
   Body / Update Parameters**.

Your adaptor is now created and ready to use. To close the adaptor
configuration page, click the **X** to the right of the adaptor name in
the tab bar near the top of the webpage.

Recipient and sender
--------------------

|acquia-product:aj| supports most common email envelope fields,
including From, To, carbon copy (CC), blind carbon copy (BCC), and
Reply-to. It is recommended that you use the descriptive format for
envelope fields (for example, ``User Name``).

To send to multiple recipients, provide the recipients as an array in
the following format:

``["Support account ", "Another user "]``

Email subject
-------------

The **Email Subject** line can be any parameterised string. The
parameter names are enclosed in ``%%`` markers.

Example
~~~~~~~

The following example provides a subject that includes a parameter that
personalizes the subject with the user's first name:

``Hello %%firstName%% Welcome to |acquia-product:aj|``

Email body
----------

The **Message Body** area can contain any valid parameterized HTML. This
will be used as the body of the email and will be rendered by the email
client. Whenever a new parameter is added to the **Subject** or the
**Message Body** it is necessary to click **Save Subject & Message Body
/ Update Parameters**. Any new parameters will then appear in the bottom
half of the page and will need to be populated before the adaptor is
valid.

Preview email
-------------

After the adaptor is valid, you can click **Preview E-mail** to preview
how the email body may appear. It is also recommended that you test your
HTML email in many email clients before using in production.

The email preview displays the parameters in the **Message Body**.

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Adaptor does not have           | It is necessary to create a       |
| connection set**                  | connection and choose it from the |
|                                   | Adaptor Connection drop down      |
+-----------------------------------+-----------------------------------+
| **E-mail write needs a 'To' data  | A valid data source for the email |
| source**                          | recipient has not been set        |
+-----------------------------------+-----------------------------------+
| **E-mail write needs a 'From'     | A valid data source for the email |
| data source**                     | sender has not been specified     |
+-----------------------------------+-----------------------------------+
| **E-mail write needs a subject**  | A Subject for the email write     |
|                                   | adaptor is mandatory. It is good  |
|                                   | practice to personalize the       |
|                                   | subject as this cuts down on the  |
|                                   | possibility of the email being    |
|                                   | mistaken for spam.                |
+-----------------------------------+-----------------------------------+
| **E-mail write needs a message**  | No message body has been          |
|                                   | provided.                         |
+-----------------------------------+-----------------------------------+
| **Received email body appears as  | One or more of the parameters is  |
| 'error'**                         | not populated in the schema when  |
|                                   | the email is created.             |
+-----------------------------------+-----------------------------------+

.. |left arrow| image:: https://cdn4.webdamdb.com/100th_sm_kR0cgUi72rf3.png?1526475474
   :class: no-sb
   :width: 24px
