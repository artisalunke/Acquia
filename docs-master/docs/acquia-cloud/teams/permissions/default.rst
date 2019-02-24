.. include:: /common/global.rst

Default |acquia-product:ac| user permissions
============================================

|userroles|_ have multiple permission levels. These permissions are dependent on
subscription type, and `can be
modified </acquia-cloud/teams/permissions>`__. You can check your role
permissions against the default using this list:

.. |userroles| replace:: \ |acquia-product:ac|\  user roles
.. _userroles: /acquia-cloud/teams/roles

-  *Team Lead* - Full access to subscriptions, can invite other members
   to the team
-  *Senior Developer* - Access to Dev, Stage, and Prod environments
-  *Developer* - Access to Dev and Stage environments

+-----------------+-----------------+-----------------+-----------------+
| Permission      | Developer       | Senior          | Team Lead       |
|                 |                 | Developer       |                 |
+=================+=================+=================+=================+
| Access the      | |no|            | |yes|           | |yes|           |
| Cloud API       |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Activate an     | |yes|           | |yes|           | |yes|           |
| Acquia          |                 |                 |                 |
| Subscription    |                 |                 |                 |
| add-on          |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Add or remove a | |no|            | |no|            | |yes|           |
| user of a team  |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Edit Remote     | |no|            | |no|            | |yes|           |
| Administration  |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| View Remote     | |no|            | |no|            | |yes|           |
| Administration  |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Modify cron     | |no|            | |yes|           | |yes|           |
| tasks for       |                 |                 |                 |
| non-production  |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Modify cron     | |no|            | |yes|           | |yes|           |
| tasks for the   |                 |                 |                 |
| production      |                 |                 |                 |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Add a database  | |no|            | |yes|           | |yes|           |
+-----------------+-----------------+-----------------+-----------------+
| Create database | |yes|           | |yes|           | |yes|           |
| backups for     |                 |                 |                 |
| non-production  |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Create database | |no|            | |yes|           | |yes|           |
| backups for the |                 |                 |                 |
| production      |                 |                 |                 |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Download        | |yes|           | |yes|           | |yes|           |
| database        |                 |                 |                 |
| backups for     |                 |                 |                 |
| non-production  |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Download        | |no|            | |yes|           | |yes|           |
| database        |                 |                 |                 |
| backups for the |                 |                 |                 |
| production      |                 |                 |                 |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Remove a        | |no|            | |no|            | |yes|           |
| database        |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Restore         | |yes|           | |yes|           | |yes|           |
| database        |                 |                 |                 |
| backups for     |                 |                 |                 |
| non-production  |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Restore         | |no|            | |yes|           | |yes|           |
| database        |                 |                 |                 |
| backups for the |                 |                 |                 |
| production      |                 |                 |                 |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| View database   | |yes|           | |yes|           | |yes|           |
| connection      |                 |                 |                 |
| details         |                 |                 |                 |
| (username,      |                 |                 |                 |
| password, or    |                 |                 |                 |
| hostname)       |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Add or remove   | |no|            | |yes|           | |yes|           |
| SSL             |                 |                 |                 |
| certificates    |                 |                 |                 |
| for the         |                 |                 |                 |
| non-production  |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Add or remove   | |no|            | |yes|           | |yes|           |
| SSL             |                 |                 |                 |
| certificates    |                 |                 |                 |
| for the         |                 |                 |                 |
| production      |                 |                 |                 |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Add or remove   | |no|            | |yes|           | |yes|           |
| domains for     |                 |                 |                 |
| non-production  |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Add or remove   | |no|            | |yes|           | |yes|           |
| domains for the |                 |                 |                 |
| production      |                 |                 |                 |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Block Insight   | |no|            | |no|            | |yes|           |
| sites           |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Manage Insight  | |yes|           | |yes|           | |yes|           |
| alerts          |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Revoke Insight  | |no|            | |no|            | |yes|           |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Download logs   | |yes|           | |yes|           | |yes|           |
| for non         |                 |                 |                 |
| production      |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Download logs   | |no|            | |yes|           | |yes|           |
| for the         |                 |                 |                 |
| production      |                 |                 |                 |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Execute         | |no|            | |no|            | |yes|           |
| pipelines       |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Add SSH key to  | |no|            | |yes|           | |yes|           |
| git repository  |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Add SSH key to  | |no|            | |yes|           | |yes|           |
| non production  |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Add SSH key to  | |no|            | |yes|           | |yes|           |
| the production  |                 |                 |                 |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Manage SSH keys | |no|            | |yes|           | |yes|           |
+-----------------+-----------------+-----------------+-----------------+
| Edit the search | |no|            | |yes|           | |yes|           |
| schema for a    |                 |                 |                 |
| subscription    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Increase the    | |no|            | |no|            | |yes|           |
| search index    |                 |                 |                 |
| limit for a     |                 |                 |                 |
| subscription    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Configure       | |no|            | |no|            | |yes|           |
| server          |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Reboot server   | |no|            | |no|            | |yes|           |
+-----------------+-----------------+-----------------+-----------------+
| Resize server   | |no|            | |no|            | |yes|           |
+-----------------+-----------------+-----------------+-----------------+
| Suspend server  | |no|            | |no|            | |yes|           |
+-----------------+-----------------+-----------------+-----------------+
| Create a        | |yes|           | |yes|           | |yes|           |
| support ticket  |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Include as a    | |no|            | |no|            | |yes|           |
| collaborator on |                 |                 |                 |
| all tickets by  |                 |                 |                 |
| default         |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| View and edit   | |yes|           | |yes|           | |yes|           |
| any support     |                 |                 |                 |
| tickets for a   |                 |                 |                 |
| subscription    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Add an          | |no|            | |no|            | |yes|           |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Clear Varnish   | |yes|           | |yes|           | |yes|           |
| cache for       |                 |                 |                 |
| non-production  |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Clear Varnish   | |no|            | |yes|           | |yes|           |
| cache for the   |                 |                 |                 |
| production      |                 |                 |                 |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Configure       | |yes|           | |yes|           | |yes|           |
| non-production  |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Configure       | |no|            | |no|            | |yes|           |
| production      |                 |                 |                 |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Delete an       | |no|            | |no|            | |yes|           |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Deploy code,    | |no|            | |yes|           | |yes|           |
| files, or       |                 |                 |                 |
| databases to    |                 |                 |                 |
| the production  |                 |                 |                 |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Move files from | |yes|           | |yes|           | |yes|           |
| non-production  |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Move files from | |yes|           | |yes|           | |yes|           |
| production      |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Move files to   | |yes|           | |yes|           | |yes|           |
| non-production  |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Move files to   | |no|            | |yes|           | |yes|           |
| the production  |                 |                 |                 |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Pull and deploy | |yes|           | |yes|           | |yes|           |
| code, files, or |                 |                 |                 |
| databases to    |                 |                 |                 |
| non-production  |                 |                 |                 |
| environments    |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Pull files or   | |no|            | |yes|           | |yes|           |
| databases from  |                 |                 |                 |
| the production  |                 |                 |                 |
| environment     |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
