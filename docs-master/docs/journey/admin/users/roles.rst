.. include:: /common/global.rst

About |acquia-product:aj| roles
===============================

|acquia-product:aj| has two types of roles: organization roles and
project roles. You can assign a role to an individual user or a group of
users. An organization may have one or more groups, associated with one
or more users.

Organization role permissions
-----------------------------

The following table describes the permissions associated with the
*Organization* role:

+---------------------------------------------------+---------+----------+
| Permissions/Role                                  | *Owner* | *Member* |
+===================================================+=========+==========+
| Organization users: add, edit, and delete         | |yes|   | |no|     |
+---------------------------------------------------+---------+----------+
| Organization groups: add, edit, and delete        | |yes|   | |no|     |
+---------------------------------------------------+---------+----------+
| Organization projects: add, edit, and delete      | |yes|   | |no|     |
+---------------------------------------------------+---------+----------+
| *Admin* project role permissions for all projects | |yes|   | |no|     |
+---------------------------------------------------+---------+----------+

Project role permissions
------------------------

The following table describes the permissions associated with the
*Project* role:

+--------------------------------------+---------+-------------+--------------+
| Permissions/Role                     | *Admin* | *Developer* | *Strategist* |
+======================================+=========+=============+==============+
| Project roles: add and remove users  | |yes|   | |no|        | |no|         |
+--------------------------------------+---------+-------------+--------------+
| Project roles: add and remove groups | |yes|   | |no|        | |no|         |
+--------------------------------------+---------+-------------+--------------+
| Graphs: add, edit, and delete        | |yes|   | |yes|       | |no|         |
+--------------------------------------+---------+-------------+--------------+
| Connections: add, edit, and delete   | |yes|   | |yes|       | |no|         |
+--------------------------------------+---------+-------------+--------------+
| Environments: add, edit, and delete  | |yes|   | |yes|       | |no|         |
+--------------------------------------+---------+-------------+--------------+
| Versions: create, and restore        | |yes|   | |yes|       | |no|         |
+--------------------------------------+---------+-------------+--------------+
| Journeys: add, edit, and delete      | |yes|   | |yes|       | |yes|        |
+--------------------------------------+---------+-------------+--------------+
| Metrics: add, edit, and delete       | |yes|   | |yes|       | |yes|        |
+--------------------------------------+---------+-------------+--------------+
