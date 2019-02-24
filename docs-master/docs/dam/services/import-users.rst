.. include:: /common/global.rst

Importing users into |acquia-product:dam|
=========================================

You can add users to |acquia-product:dam| in bulk (greater than 50
users) by doing a user import.

A user import is included as part of the |acquia-product:dam| standard
onboarding, and is also available as an add-on service. Contact your
Acquia Account Manager for more information.

.. _specs:

User import procedure
---------------------

Be sure to complete the following steps to bulk import your
organization's users into |acquia-product:dam|:

#. `Create any needed groups </dam/admin/users#group>`__ for your users.

   .. note::
      Group roles will define the user role. For example, if a group role
      is Contributor, then the user will be imported to
      |acquia-product:dam| with a Contributor role type.

#. Complete the `user import
   spreadsheet <https://www.damsuccess.com/hc/en-us/article_attachments/203289526/User_Import_Spreadsheet_Example.xlsx>`__
   by providing the following information:

   -  Username *(required)*
   -  Email (required)
   -  First Name (required)
   -  Last Name (required)
   -  Group(s) (required)
   -  Company
   -  Company URL
   -  Phone Number
   -  Fax Number
   -  Country/State
   -  City/Town
   -  Address 1
   -  Address 2
   -  Zip/Postal Code

#. Contact your Acquia Account Manager, provide them your user import
   spreadsheet, and address the following additional items:

   -  Do you want to import your users as active or inactive?
      *Active users* will be able to sign in and browse
      |acquia-product:dam| right away.
      *Inactive users* will not be able to sign in until an admin
      activates them. Upon activation, the admin can determine whether
      an email is sent to users. Unless you create a generic password
      for the import, users will need to `create their own
      password </dam/access/password#reset>`__.
   -  If you want your users to be active upon import, do you want your
      users to be notified by email?
      If *yes*, upon import users will receive a welcome email that
      contains a link to set their own password.
      If *no*, you will need to notify your users regarding
      |acquia-product:dam| sign-in instructions. Users will need to
      `create their own password </dam/access/password#reset>`__, unless
      a generic password is created during the import process.
   -  Do you want your users to set their own passwords, or do you want
      to create a generic password?
      If you want users to *set their own passwords*, active users
      imported with an initial email sent will be prompted to create a
      password. If an email is not sent to users or your users are being
      imported as inactive users, they will need to `create their own
      password </dam/access/password#reset>`__.
      If you want to *create a generic password*, all users will receive
      the password of your choosing. Users can `change their
      password </dam/access/password>`__ after signing in.
