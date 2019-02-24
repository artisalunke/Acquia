.. include:: /common/global.rst

Problems using MySQL stored procedures, triggers, and functions
===============================================================

It is a bad practice to use stored procedures, triggers, or functions in
your Drupal database. Having code in both your version control
repository and in your database increases complexity, makes it harder to
maintain your code, and undermines recovery and other high availability
(HA) platform operational tasks. By default, code in these objects is
not maintained in version control, which makes it difficult to manage
releases without risking mismatches between PHP and SQL code. Instead,
you should implement your business logic in your Drupal application
code, not directly in your database.

Using these objects is especially bad in an HA database environment,
such as |acquia-product:ace|. In combination with the
|acquia-product:ace| database replication feature, which is an essential
element of the |acquia-product:ace| high availability architecture,
using stored procedures, triggers, or MySQL functions can result in
security risks, replication conflicts, and application errors, due to
mismatches between your Drupal codebase and code in MySQL (for example,
after a code rollback).

To avoid this problem, |acquia-product:ace| has disabled the use of
stored procedures, triggers, or MySQL functions in all environments.
This will not affect existing stored procedures, triggers, or MySQL
functions, but will trigger errors if you modify them.
