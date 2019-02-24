.. include:: /common/global.rst

Creating custom Insight tests
=============================

|acquia-product:ais| provides dozens of tests to check your
application's conformance with best practices for security, performance,
and general Drupal and web application development. In addition, Insight
enables you to develop your own custom Insight tests. Your custom
Insight tests can check for aspects of your applications that are most
important to your own business needs.

Creating a custom Insight test requires that you write PHP code and
create and deploy a custom Drupal module. You will need to create a
custom Drupal module that implements ``hook_acquia_spi_test();``, and
then install and enable it on your Drupal application.

Data sent in a custom Insight test is stored on Acquia's servers in an
unencrypted database, so be careful not to send sensitive information in
any field. You can include multiple tests in each callback, provided
that each test has a unique identifier.

Your custom Insight test module must implement
``hook_acquia_spi_test();`` in order to send test data back to Insight,
so that the test results can be reported in Insight and reflected in
your application's Insight score. This hook must return an array that
contains the test that you want to use and the results for success or
failure. The array includes the following elements:

+-----------------------+-----------------------+-----------------------+
| Array element         | Type                  | Description           |
+=======================+=======================+=======================+
| ``description``       | string                | Detailed information  |
|                       |                       | regarding the test,   |
|                       |                       | its impact, and other |
|                       |                       | relevant details.     |
|                       |                       | Cannot exceed 1024    |
|                       |                       | characters.           |
+-----------------------+-----------------------+-----------------------+
| ``solved_message``    | string                | The message to        |
|                       |                       | display when the test |
|                       |                       | succeeded. Cannot     |
|                       |                       | exceed 1024           |
|                       |                       | characters.           |
+-----------------------+-----------------------+-----------------------+
| ``failed_message``    | string                | The message to        |
|                       |                       | display when the test |
|                       |                       | has failed. Cannot    |
|                       |                       | exceed 1024           |
|                       |                       | characters.           |
+-----------------------+-----------------------+-----------------------+
| ``solved``            | boolean               | A flag indicating     |
|                       |                       | whether or not the    |
|                       |                       | test was successful.  |
+-----------------------+-----------------------+-----------------------+
| ``fix_details``       | string                | Information on how to |
|                       |                       | fix or resolve the    |
|                       |                       | test if it failed.    |
|                       |                       | Cannot exceed 1024    |
|                       |                       | characters.           |
+-----------------------+-----------------------+-----------------------+
| ``category``          | string                | The Insight alert     |
|                       |                       | category within which |
|                       |                       | to place the test.    |
|                       |                       | Must be either        |
|                       |                       | 'performance,'        |
|                       |                       | 'security,' or        |
|                       |                       | 'best_practices.'     |
+-----------------------+-----------------------+-----------------------+
| ``severity``          | int                   | The severity level of |
|                       |                       | the custom test. Must |
|                       |                       | be either 0, 1, 2, 4, |
|                       |                       | 8, 16, 32, 64, or     |
|                       |                       | 128. Higher           |
|                       |                       | severities impact the |
|                       |                       | Insight score         |
|                       |                       | proportionally.       |
+-----------------------+-----------------------+-----------------------+

Here is a simple example that tests whether the user with the provided
user ID has the administrator role:

.. code-block:: php

   /**  
   * Check if a user has the administrator role.  
   *  
   * @param int $uid  
   *  The UID of the user to audit. 
   *   
   * @return boolean  
   *  TRUE if the provided user has the administrator role.  
   *  
   */ function acquia_examples_admin_role_audit($uid) 
    {    $result = TRUE;    $user = user_load($uid);   
    if (!in_array('administrator', $user->roles)) {     
    $result = FALSE;   }    
    return $result; }

In your test callback function, return an array for each test you
include. For example:

.. code-block:: php

   /**  * Implements hook_acquia_spi_test(). Example usages of properly formatted  
   * Acquia Insight custom tests.  
   *  
   * @see acquia_connector/acquia_spi/acquia_spi.api.php for more information.  
   *  
   */ function acquia_examples_acquia_spi_test() {    
    return array(     
    // Ensure that user 1 has administrator privileges.    
     'user_1_admin_privileges_check' => array(       
      'description'    => 'Check if the user UID 1 has administrator privileges.',       
      'solved_message' => 'Admin User (UID 1) has administrator privileges',       
      'failed_message' => 'Admin User (UID 1) lacks administrator privileges',       
      'solved'         => acquia_examples_admin_role_audit(1),       
      'fix_details'    => 'Give user UID 1 administrator privileges.',       
      'category'       => 'security',       
      'severity'       => 32,  
         ), 
        ); 
        }

Note how the solved element tests whether, given user ID 1, the
``acquia_examples_admin_role_audit`` function defined in the previous
example returns ``TRUE``.

For more examples, `download this custom
module </sites/default/files/doc/2013/sep/acquia_examples.zip>`__.
