.. include:: /common/global.rst

Factory API examples
====================

The Factory API (included with |acquia-product:edg|) enables you to
interact with |acquia-product:edg| from the command line by scripting
frequently-repeated events.

For information about obtaining your API key or basic usage of the
Factory API, see `Using the |acquia-product:edg| REST
API </site-factory/extend/api>`__.

The following example scripts were created by |acquia-product:edg|
users, and can be adapted where necessary to meet your needs:

-  `Synchronizing production and development environments <#synchronizing-production-and-development-environments>`__
-  `Initiating code releases <#initiating-code-releases>`__


Synchronizing production and development environments
-----------------------------------------------------

The following script allows you to initiate the website staging process
to an environment that you specify, after modifying it to fit your
environment's needs:

.. code-block:: none

   #!/usr/bin/env bash
   ## Synchronizing production and development environments on Acquia Cloud Site Factory
   ## Origin: http://docs.acquia.com/site-factory/extend/api/examples

   #!/bin/sh

   # Update the next two lines to provide your ACSF username and API key
   user="[your_ACSF_username]"
   api_key="[your_API_key]"

   # Machine name of target environment
   to_acsf_environment="dev"

   # Update the next line to provide a comma-separated list of site IDs
   sites="[123,456]"

   # Update the next line to provide your Acquia Cloud Site Factory domain name
   curl 'https://www.[domain].acsitefactory.com/api/v1/stage' \
      -X POST -H 'Content-Type: application/json' \
      -d "{"to_env": "${to_acsf_environment}", "sites": [ ${sites} ], "detailed_status": true}" \
      -v -u $user:$api_key


Initiating code releases
------------------------

The following script begins a code and database update for the
environment that you specify.

.. code-block:: bash

   #!/bin/sh
   ## Initiate a code and database update from Acquia Cloud Site Factory
   ## Origin: http://docs.acquia.com/site-factory/extend/api/examples

   # This script should primarily be used on non-production environments.
   # To run on a production environment, change the domain name in the
   # curl command and remove the "-k" parameter

   # Update the next two lines to provide your ACSF username and API key
   user="[your_ACSF_username]"
   api_key="[your_API_key]"

   # Machine name of target ACSF environment. 
   env="dev"

   # Provide the name of the branch or tag to update code with
   sites_ref="[develop-build]"

   # What should be updated? Use "code" if we only want to update code, or 
   # "code,db" if we want to deploy code and database
   sites_type="code,db"

   # add comma to "code,db" if not already entered
   if [ "$sites_type" == "code,db" ]
   then
      sites_type="code, db"
   fi

   # Replace [domain] on the following line with your Acquia Cloud Site Factory domain name
   curl "https://www.${env}-[domain].acsitefactory.com/api/v1/update" \
   -v -u ${user}:${api_key} -k -X POST \
   -H 'Content-Type: application/json' \
   -d "{"sites_ref": "${sites_ref}", "sites_type": "${sites_type}"}"