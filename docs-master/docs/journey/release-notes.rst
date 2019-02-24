.. include:: /common/global.rst

Release notes - Acquia Journey
==============================

Looking for the latest and greatest new features and changes to |acquia-product:aj|? Read on and check back regularly to see what else we’ve done.

.. _20180424:

Acquia Journey - 1.12.3
----------------------------
*Tue, 24 Apr 2018*

This release of Acquia Journey contains the following updates:

Change
~~~~~~

-  Improved the handling of graphs with longer execution times to avoid
   error messages being displayed.

Fixed issue
~~~~~~~~~~~

-  Whenever an organization had no available
   `metrics </journey/metrics>`__ data, the Acquia Journey interface
   became unresponsive.

.. _20180404:

Acquia Journey - 1.12.1
----------------------------
*Wed, 4 Apr 2018*

This release of Acquia Journey contains the following updates:

Feature
~~~~~~~

-  **Use Amazon S3 file storage from within your graphs**
   You now integrate cloud file storage into your graphs with the S3
   `file adaptor </journey/adaptors/file>`__, enabling you to retrieve
   existing files and upload new files.

Changes
~~~~~~~

-  When browsing the `Schema location </journey/data#schema>`__, you can
   now filter by field name by entering the first few letters of a field
   name in the search box.
-  The `Graph API listener </journey/adaptors/graph-api>`__ now accepts
   a ``POST`` body with ``Content-Type: XML``.
-  Improved performance of the Acquia Journey user interface.

Fixed issues
~~~~~~~~~~~~

-  In situations involving large schema elements, the data was not
   always handled correctly.
-  When filtering the schema location, arrays were not handled properly.
-  UTF-8 characters were not always properly encoded.

.. _20180208:

Acquia Journey - 1.11.2
----------------------------
*Thu, 8 Feb 2018*

This release of Acquia Journey contains the following updates:

Resolved security issues
~~~~~~~~~~~~~~~~~~~~~~~~

-  Applied patches for Spectre vulnerability.
-  Applied patches for Meltdown vulnerability.

Feature
~~~~~~~

-  **More easily start creating journeys with pre-made graph templates**
   To help you get started with Acquia Journey and create graphs more
   quickly, there are now several ready-made graph templates included
   with the product for your use. `Learn
   more </journey/getting-started/graph/template>`__.

Changes
~~~~~~~

-  The email write adaptor now allows you to configure the carbon copy
   (CC), blind carbon copy (BCC), and reply-to fields. `Learn
   more </journey/adaptors/email/write>`__.
-  Whenever users are signed out due to inactivity, users are redirected
   to the main Acquia Journey sign-in page.
-  Visitor query is now available as an action for the Acquia Lift
   adaptor. `Learn more </journey/adaptors/lift/visitor>`__.
-  When configuring a `message queue
   connection </journey/connect/message>`__ for Amazon web services
   (AWS), the AWS secret key is treated as a password and masked when
   entered.
-  Acquia Journey has several improvements that don't necessarily affect
   your use of the product, in the following areas:

   -  Password security improvements
   -  Improved compatibility of `Graph API
      listener </journey/adaptors/graph-api>`__ web tracking and jQuery
   -  Performance improvements in the `Graph
      API </journey/adaptors/graph-api>`__

Fixed issues
~~~~~~~~~~~~

-  The following features received fixes in this release due to
   discovered issues:

   -  Security fix - Integer overflow
   -  Security fix - Cross-site scripting (XSS) vulnerability
   -  `Testing console </journey/getting-started/test#console>`__ - Data
      display issue

-  In some situations, the `SOAP adaptor </journey/adaptors/soap>`__
   parsed WSDL incorrectly.
-  Graphs hydrated from a `graph
   template </journey/getting-started/graph/template>`__ using
   `parameters </journey/getting-started/graph#parameters>`__ were
   missing a data source.
-  In certain circumstances, the Acquia Journey graph engine would fail.
-  Occasionally, pointing to `data schema </journey/data>`__ actions
   displayed help text in the incorrect location.

.. _20171101:

Acquia Journey - 1.1
-------------------------
*Wed, 1 Nov 2017*

This release of Acquia Journey contains the following updates:

Changes
~~~~~~~

-  When creating a new node in a graph, you can choose `from a list of
   managed graphs </journey/node/managed-graph>`__ provided and managed
   by Acquia, but you cannot directly edit a managed graph.
-  When used as a subgraph, graphs may now attach a listener, or `accept
   parameters </journey/getting-started/graph#parameter>`__ passed from
   the schema, but not both.
-  Acquia Journey now supports the Azure Service Bus as a `message queue
   connection type </journey/connect/message>`__.
