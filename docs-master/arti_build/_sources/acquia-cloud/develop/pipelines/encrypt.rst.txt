.. include:: /common/global.rst

Encrypting keys and variables
=============================

A build definition file may need to include sensitive information, such
as SSH keys or passwords that are needed to access private resources,
but you do not want to include these in plain text in your build
definition file. You can encrypt this sensitive information, and then
use the encrypted value in a ``secure`` element in the build definition
file.

.. _encrypt:

Encrypting your information
---------------------------

You can use either the |acquia-product:ac| interface or the command line
to encrypt your variables and keys that are to be stored with your
codebase. Follow the procedures based on your selected method:

-  *Using the |acquia-product:ac| interface*

   #. Sign in to the `|acquia-product:ac|
      interface <https://cloud.acquia.com>`__.
   #. Select the application that you want to use.
   #. In the left menu, click **Pipelines**.
   #. | Click **More Links**.

      |More Links icon|

   #. Click **Encrypt Credentials**.
   #. To encrypt an environment variable, click **Environment
      Variable**, and type the name of your variable and its value into
      the fields provided.
   #. To encrypt an SSH key, click **SSH Keys**, and then use one of the
      following methods to provide the contents of your key:

      -  Drag your key into the box to copy its contents; the field will
         turn blue to indicate when you've dragged it to the correct
         place.
      -  Copy and paste the contents of your key into the field.

   #. Click **Encrypt**. The encrypted version of your information will
      appear in the box to the right.
   #. Click the **Copy** icon |Copy icon| to copy the encrypted
      information to your clipboard.
   #. Click **Close**.

-  *Using the command line*
   To encrypt an SSH private key, execute the following command,
   replacing ``[~/.ssh/id_rsa]`` with the actual path to the SSH private
   key you want to encrypt:

   ``cat [~/.ssh/id_rsa] | pipelines encrypt -``

   To encrypt arbitrary text (such as a password), use the following
   command, replacing ``my password`` (but not the enclosing quotation
   marks) with your text:

   ``echo “my password” | pipelines encrypt -``

   Note

   Additional command-line encryption examples are available in the `301
   tutorial - Accessing private
   repositories <https://github.com/acquia/pipelines-examples/tree/master/tutorial-301>`__
   example on GitHub.

You are now ready to add your encrypted information to your code
repository.

.. _placement:

Placing encrypted information in your codebase
----------------------------------------------

Regardless of what encrypted information you are adding to your
codebase, after adding the information, be sure to commit your changes
to your code repository.

Encrypted SSH keys should be stored in the ``ssh-keys`` element of your
``acquia-pipelines.yaml`` file with a name of your choosing. For
example:

``ssh-keys:   mykey:      secure: 2acIshWAndTh1sG0esOn . . .``

The decrypted SSH private key will then be available during your build.

Encrypted variables should be stored in the ``variables`` element of
your ``acquia-pipelines.yaml`` file with a variable name of your
choosing. For example:

``variables:   global:     PASSWORD:       secure: 2acqDl…``

The decrypted value will be available as an environment variable during
your build.

Note

For more information about the ``acquia-pipelines.yaml`` file, see
`Creating and managing your build definition
file </acquia-cloud/develop/pipelines/yaml>`__.

.. |More Links icon| image:: https://cdn3.webdamdb.com/310th_sm_UIzMSRVRQXA0.png?1526475481
   :width: 273px
   :height: 78px
.. |Copy icon| image:: https://cdn2.webdamdb.com/100th_sm_MmwLNeGf0b31.png?1526475798
   :width: 25px
   :height: 26px
