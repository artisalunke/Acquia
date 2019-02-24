.. include:: /common/global.rst

Container resources
===================

|acquia-product:ac|-provided containers provide the following resources,
tools, and PHP extensions, which you can use with your build processes.

-  `Specifications and resource limits <#specs>`__
-  `Tools <#tools>`__
-  `PHP extensions <#extensions>`__

.. note::

    For information about the software resources included with
    |acquia-product:ac| applications, which are separate from the software
    in the |acquia-product:ac| containers, see |acquia-product:ac| `technology 
    platform and supported software </acquia-cloud/arch/tech-platform>`__.

.. _specs:

Specifications and resource limits
----------------------------------

Jobs executed in your container have the following resource limits:

-  1.6GB of memory
-  8GB of disk space
-  One hour of running time per job
-  Maximum of two concurrent jobs

Tools
-----

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Resource
     - Version
   * - acquia-yaml
     - 1.0.4
   * - Bundler
     - 1.15.1
   * - bzip2
     - 1.0.6
   * - Composer
     - 1.5.1
   * - `Drush </acquia-cloud/container/drush>`__
     - 8.1.12 (default), 7.4.0, and 6.7.0
   * - Fontconfig
     - 2.11.0
   * - Gem
     - 2.6.12
   * - Git
     - 2.1.4
   * - Google Chrome
     - 59.0.3071
   * - imagemagick
     - 6.8.9-9
   * - MySQL
     - 5.6.36
   * - Node.js
     - 4.8.4
   * - npm
     - 2.15.11
   * - nvm
     - 0.33.2
   * - patch
     - 2.7.5
   * - PHP
     - 5.6.31 (CLI), 7.1.8, Zend Engine 2.6.0
   * - rbenv
     - 1.1.1, 2.3.4, 2.4.1
   * - rsync
     - 3.1.1
   * - Ruby
     - 2.3.4 (default), 2.4.1
   * - SSH
     - OpenSSH_6.7p1 Debian-5, OpenSSL 1.0.1k
   * - unzip
     - 6.00
   * - wget
     - 1.16

.. _extensions:

PHP extensions
--------------

+-----------+------------------------------------------------------+
| Extension | Version                                              |
+===========+======================================================+
| bcmath    |                                                      |
+-----------+------------------------------------------------------+
| bz2       | 1.0.6                                                |
+-----------+------------------------------------------------------+
| gd        | bundled (2.1.0 compatible)                           |
+-----------+------------------------------------------------------+
| gmp       | 6.0.0                                                |
+-----------+------------------------------------------------------+
| imagick   | 3.4.3                                                |
+-----------+------------------------------------------------------+
| mcrypt    | 2.5.8; API number 20021217                           |
+-----------+------------------------------------------------------+
| mysqli    | mysqlnd 5.0.11-dev - 20120503                        |
+-----------+------------------------------------------------------+
| pcntl     |                                                      |
+-----------+------------------------------------------------------+
| pdo_mysql | mysqlnd 5.0.11-dev - 20120503                        |
+-----------+------------------------------------------------------+
| xsl       |                                                      |
+-----------+------------------------------------------------------+
| yaml      |                                                      |
+-----------+------------------------------------------------------+
| zip       | extension - ccd0467fd353f0f5c2d8834a51ab217aa6053e0d |
|           | zip - 1.12.5                                         |
+-----------+------------------------------------------------------+
