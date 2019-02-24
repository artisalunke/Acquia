.. include:: /common/global.rst

Acquia Lift architecture
========================

.. toctree::
  :hidden:
  :glob:

  /lift/arch/*

This page describes how Acquia delivers high availability in
|acquia-product:cha|, and how |acquia-product:cha| handles disaster
recovery and backups.

High availability data centers
------------------------------

|acquia-product:cha| is located in data centers that are physically
remote from Acquia’s office facilities. Because of this, a disaster
affecting one or more of Acquia's offices would not impact the
availability of |acquia-product:cha|.

The |acquia-product:cha| environment consists of major regions and
Availability Zones. Availability Zones are separate, yet interconnected,
data centers within major regions in Acquia’s global infrastructure.
|acquia-product:cha| supports the following zones:

-  US (East)
-  EU (Frankfurt)
-  Asia Pacific (Sydney)

Disaster recovery
-----------------

For disaster recovery purposes, |acquia-product:cha| performs
synchronous replication of person data across Availability Zones, hourly
snapshots of document data, and daily snapshots of customer
configuration and data warehouse databases. These backups will be used
to restore |acquia-product:cha| at another location in the same region
in the event of either a total data center loss or a loss of multiple
disk systems. Acquia will not provide customer access to these
snapshots, and will not use these snapshots to restore data due to
data-loss or deletion by customers.

Backups
-------

Acquia maintains a backup solution for all components of
|acquia-product:cha|, including the following:

-  All documents persisted in |acquia-product:ch|. |br|
   The backups are based on a combination of synchronous replications of
   documents across Availability Zones and hourly snapshots of document
   data.
-  All documents persisted in |acquia-product:lpm| and
   |acquia-product:leb|, including person profile, customer
   configuration, and data warehouse databases. |br|
   The backups are based on a combination of synchronous replication of
   person profile data across Availability Zones and daily snapshots of
   the customer configuration and data warehouse databases.
