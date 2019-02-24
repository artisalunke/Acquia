.. include:: /common/global.rst

Using the |acquia-product:dam| API
==================================

The |acquia-product:dam| API is the underlying interface for building
apps using the power of |acquia-product:dam|. The API allows developers

to securely read and write from |acquia-product:dam| so your users can
push and pull their important files and metadata. You will also have
access to powerful |acquia-product:dam| features such as file sharing,
upload, search, and more.

To use the API, you'll need to create and use an admin account in
|acquia-product:dam|. Be sure to ask your |acquia-product:dam|
administrator to assist you with an account if you do not already have
one.

If API usage/analytics is important to your organization, consider using
a unique admin seat for the API.

|acquia-product:dam| REST API v2
--------------------------------

Accessing the API
~~~~~~~~~~~~~~~~~

-  `Connecting to |acquia-product:dam| REST API V2 <#api_connecting>`__
-  `Important keys <#api_important_keys>`__
-  `Authorize the user <#api_authorize_user>`__
-  `Store the authorization_code <#api_store_code>`__
-  `Getting the access_token and refresh_token <#api_get_token>`__
-  `Getting the access_token using grant type
   "password" <#api_get_token_password>`__
-  `An Example: Retrieving folders from your account <#api_example>`__
-  `Resetting the access_token <#api_resetting>`__

Folders
~~~~~~~

-  `Folder JSON Format <#folderjson>`__
-  `View top level folders <#gettoplevelfolders>`__
-  `Get folder information <#getfolder>`__
-  `Get multiple folder information <#getmultifolder>`__
-  `Create a folder <#createfolder>`__
-  `Edit a folder <#editfolder>`__
-  `Delete a folder <#deletefolder>`__
-  `List assets for a folder <#getfolderassets>`__

Assets
~~~~~~

-  `Asset JSON Format <#assetjson>`__
-  `Get asset information <#getasset>`__
-  `Get multiple asset information <#getmultiasset>`__
-  `Edit an asset <#editasset>`__
-  `Delete an asset <#deleteasset>`__
-  `Upload an asset (optimized) <#uploadasset>`__
-  `Download an asset <#downloadasset>`__
-  `View versions of an asset <#viewassetversions>`__
-  `Get an asset version <#getassetversion>`__
-  `Delete an asset version <#deleteassetversion>`__
-  `Restore an asset version <#restoreassetversion>`__
-  `Download an asset version <#downloadassetversion>`__
-  `Get related assets for an asset <#assetrelated>`__
-  `Send asset download <#sendassetdownload>`__

Metadata
~~~~~~~~

-  `View asset XMP metadata <#getassetxmp>`__
-  `Edit asset XMP metadata <#editassetxmp>`__
-  `View asset EXIF metadata <#getassetexif>`__

Metadata Templates
~~~~~~~~~~~~~~~~~~

-  `Get all metadata templates <#getmetadatatemplates>`__
-  `Get a metadata template <#getmetadatatemplate>`__
-  `Create a metadata template <#createmetadatatemplate>`__
-  `Edit a metadata template <#editmetadatatemplate>`__
-  `Delete a metadata template <#deletemetadatatemplate>`__
-  `Apply a metadata template to folders <#applymetadatatemplate>`__

Metadata Schema
~~~~~~~~~~~~~~~

-  `Get metadata schema <#getmetadataschema>`__
-  `Update metadata type <#updatemetadatatype>`__

Lightboxes
~~~~~~~~~~

-  `Lightbox JSON Format <#lightboxjson>`__
-  `Get current users lightboxes <#getlightboxes>`__
-  `Get a lightbox <#getlightbox>`__
-  `Create a lightbox <#createlightbox>`__
-  `Edit a lightbox <#editlightbox>`__
-  `Delete a lightbox <#deletelightbox>`__
-  `List assets for a lightbox <#getlightboxassets>`__
-  `Add asset to a lightbox <#addlightboxasset>`__
-  `Remove asset from a lightbox <#removelightboxasset>`__
-  `Empty a lightbox <#emptylightbox>`__
-  `List collaborators for a lightbox <#getlightboxcollaborators>`__
-  `Add collaborator to a lightbox <#addlightboxcollaborator>`__
-  `Remove a collaborator from a
   lightbox <#removelightboxcollaborator>`__
-  `Send lightbox download <#sendlightboxdownload>`__

Lightboxes Comments
~~~~~~~~~~~~~~~~~~~

-  `List comments on a lightbox <#getlightboxcomments>`__
-  `Get a lightbox comment <#getlightboxcomment>`__
-  `Add comment to a lightbox <#addlightboxcomment>`__
-  `Delete a comment from a lightbox <#deletelightboxcomment>`__
-  `List comments on an asset in lightbox <#getlightboxassetcomments>`__
-  `Get comment on an asset in lightbox <#getlightboxassetcomment>`__
-  `Add comment to an asset in lightbox <#addlightboxassetcomment>`__
-  `Delete a comment on an asset in
   lightbox <#deletelightboxassetcomment>`__

Groups
~~~~~~

-  `Group JSON Format <#groupjson>`__
-  `Get all groups <#getgroups>`__
-  `Get a group <#getgroup>`__
-  `Create a group <#creategroup>`__
-  `Edit a group <#editgroup>`__
-  `Delete a group <#deletegroup>`__
-  `View users of a group <#getgroupusers>`__
-  `Add user to group <#addusertogroup>`__
-  `Remove user from group <#removeuserfromgroup>`__

Users
~~~~~

-  `User JSON Format <#userjson>`__
-  `Get users <#getusers>`__
-  `Get current user <#getcurrentuser>`__
-  `Get a user <#getuser>`__
-  `View groups for a user <#getusergroups>`__
-  `Create a user <#createuser>`__
-  `Edit a user <#edituser>`__
-  `Delete a user <#deleteuser>`__

Account
~~~~~~~

-  `Get account subscription <#accountsubscription>`__

Notifications
~~~~~~~~~~~~~

-  `Available actions <#availablenotificationtypes>`__
-  `Get notifications <#getnotifications>`__

API Reference
~~~~~~~~~~~~~

-  `Exif Metadata <#exif-metadata>`__
-  `XMP Metadata <#xmpiptc-metadata>`__

.. _accessing-the-api-1:

Accessing the API
-----------------

.. _api_connecting:

Connecting to |acquia-product:dam| REST API V2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before performing any API calls, your application needs to authenticate
with the |acquia-product:dam| OAuth2 server, and your users need to sign
in so that they can perform authenticated web service requests. For this
you need to first obtain an application ID, which you will then use to
connect to the |acquia-product:dam| OAuth2 servers. To obtain an
application ID, `contact Acquia Support </support#contact>`__.

.. _api_important_keys:

Important keys
~~~~~~~~~~~~~~

The following information is required for accessing the
|acquia-product:dam| Authorization APIs.

+-----------------------------------+-----------------------------------+
| Key                               | Description                       |
+===================================+===================================+
| CLIENT_ID                         | Contact your Account Manager or   |
|                                   | `Acquia                           |
|                                   | Support </support#contact>`__ for |
|                                   | the CLIENT_ID.                    |
+-----------------------------------+-----------------------------------+
| CLIENT_SECRET                     | Contact your Account Manager or   |
|                                   | `Acquia                           |
|                                   | Support </support#contact>`__ for |
|                                   | the CLIENT_ID.                    |
+-----------------------------------+-----------------------------------+
| REDIRECT_URI                      | This is the client URL to         |
|                                   | redirect back to after            |
|                                   | successfully signing in.          |
+-----------------------------------+-----------------------------------+
| ACCESS_CODE                       | This is used to request an        |
|                                   | access_token. Lifetime of 30      |
|                                   | seconds.                          |
+-----------------------------------+-----------------------------------+
| ACCESS_TOKEN                      | This is used to make API calls on |
|                                   | behalf of a user. Lifetime of 1   |
|                                   | hour.                             |
+-----------------------------------+-----------------------------------+
| REFRESH_TOKEN                     | This is used for refreshing the   |
|                                   | access token.                     |
+-----------------------------------+-----------------------------------+

.. _api_authorize_user:

Authorize the user
~~~~~~~~~~~~~~~~~~

After your application knows that the user needs to be authenticated,
your application shall redirect the user to the following URL so that
the user can authorize your application:

``https://apiv2.webdamdb.com/oauth2/authorize?response_type=code&client_id=CLIENT_ID&redirect_uri=REDIRECT_URI&state=STATE``

The user will sign in with their |acquia-product:dam| credentials, and
then they will be required to authenticate your application to use their
data.

After the user makes the authorization, |acquia-product:dam| will
redirect back to your application and also send a temporary
authorization_code in the GET of the redirect URL. An example of the
redirect path is:

``http://yourdomain.com/?code=AUTHORIZATION_CODE&state=STATE``

Your application will then use this authorization_code to fetch an
access_token and refresh_token. The access_token will allow your
application to perform subsequent service calls on behalf of the user.
The state variable will also be forwarded to the redirect URL to help
validate the request.

.. _api_store_code:

Store the authorization_code and refresh_token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your application should store the authorization_code and refresh_token
retrieved above for subsequent calls to the |acquia-product:dam| APIs.

.. _api_get_token:

Getting the access_token
~~~~~~~~~~~~~~~~~~~~~~~~

After the code has been obtained, it may be used to request the
access_token that will be used to retrieve data on behalf of the user
from |acquia-product:dam|.

.. code::

  curl -X POST https://apiv2.webdamdb.com/oauth2/token -d 'grant_type=authorization_code&code=AUTHORIZATION_CODE&redirect_uri=REDIRECT_URI&client_id=CLIENT_ID&client_secret=SECRET_KEY'

This will return a response which contains keys that will be used to
refresh your API session or to get data from |acquia-product:dam|:

.. code:: json

  {
      "access_token":"ACCESS_TOKEN",
      "expires_in":3600,
      "token_type":"bearer",
      "refresh_token":"REFRESH_TOKEN"
  }

.. _api_get_token_password:

Getting the access_token using grant type "password"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have a trusted relationship with the user you can supply the the
user credentials directly to get an access_token without needing to get
an authorization_code first.

+-----------------------------------+-----------------------------------+
| Key (Grant Type: password)        | Description                       |
+===================================+===================================+
| CLIENT_ID                         |                                   |
+-----------------------------------+-----------------------------------+
| CLIENT_SECRET                     |                                   |
+-----------------------------------+-----------------------------------+
| USERNAME                          |                                   |
+-----------------------------------+-----------------------------------+
| PASSWORD                          |                                   |
+-----------------------------------+-----------------------------------+
| ACCESS_TOKEN                      | This is used to make API calls on |
|                                   | behalf of a user. Lifetime of 1   |
|                                   | hour.                             |
+-----------------------------------+-----------------------------------+
| REFRESH_TOKEN                     | This is used for refreshing the   |
|                                   | access token.                     |
+-----------------------------------+-----------------------------------+

``curl -X POST https://apiv2.webdamdb.com/oauth2/token -d 'grant_type=password&client_id=CLIENT_ID&client_secret=SECRET_KEY&username=USERNAME&password=USER_PASSWORD'``

This will return a response which contains keys that will be used to
refresh your API session or to get data from |acquia-product:dam|:

.. code:: json

  {
    "access_token":"ACCESS_TOKEN",
    "expires_in":3600,
    "token_type":"bearer",
    "refresh_token":"REFRESH_TOKEN"
  }

.. _api_example:

An Example: Retrieving folders from your account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you have the ``access_token`` from the call above, you can use it
to get folders from |acquia-product:dam| by performing the following
service call:

``curl -H "Authorization: Bearer ACCESS_TOKEN" https://apiv2.webdamdb.com/folders``

This may return a response as shown:

.. code:: json

  [
    {
        "type":"folder",
        "id":"182378912893",
        "parent":"0",
        "name":"Movies",
        "status":"active",
        "datecreated":"2013-07-18 07:03:00",
        "passwordprotected":"false",
        "user":{
          "type":"user",
          "id":"32326",
          "email":"testing@yourdomain.com",
          "name":"John Smith",
          "username":"jsmith"
        },
        "numassets":"2",
        "numchildren":1,
        "permissions":{
          "folders":[
              "create",
              "move",
              "delete",
              "edit"
          ],
          "assets":[
              "download",
              "upload",
              "move",
              "edit",
              "delete"
          ]
        },
        "thumbnailurls":[
          {
              "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_DSF3243S.jpg"
          },
          {
              "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_DSF3243S.jpg"
          },
          {
              "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_DSF3243S.jpg"
          },
          {
              "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_DSF3243S.jpg"
          }
        ]
    }
  ]

.. _api_resetting:

Resetting the access_token
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to make service calls on a regular basis and you need a
greater time to keep for the access_token, you may request a refresh
service to re-enable the session of your access_token.

This is done using the following refresh call:

``curl -H "Authorization: Bearer ACCESS_TOKEN" https://apiv2.webdamdb.com/oauth2/token -d 'grant_type=refresh_token&refresh_token=REFRESH_TOKEN&client_id=CLIENT_ID&client_secret=SECRET_KEY&redirect_uri=REDIRECT_URI' -X POST``

.. note:: The refresh_token required above is received using the access_token
          request, see ‘Getting the access_token’ above.

.. _folders-1:

Folders
-------

.. _folderjson:

Folder JSON Format
~~~~~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Attribute             | Type                  | Description           |
+=======================+=======================+=======================+
| type                  | string                | This is equal to      |
|                       |                       | "folder".             |
+-----------------------+-----------------------+-----------------------+
| id                    | long                  | The unique id of the  |
|                       |                       | folder.               |
+-----------------------+-----------------------+-----------------------+
| metadatatemplateid    | long                  | The associated        |
|                       |                       | metadata template id  |
|                       |                       | for a folder, if      |
|                       |                       | available. Default    |
|                       |                       | value is null.        |
+-----------------------+-----------------------+-----------------------+
| parent                | string                | The id of the folder  |
|                       |                       | the folder is located |
|                       |                       | in. Value of 0 means  |
|                       |                       | its at the root.      |
+-----------------------+-----------------------+-----------------------+
| name                  | string                | The name of the       |
|                       |                       | folder.               |
+-----------------------+-----------------------+-----------------------+
| status                | string                | The current state of  |
|                       |                       | the folder, either    |
|                       |                       | active or inactive.   |
+-----------------------+-----------------------+-----------------------+
| user                  | Mini user             | The mini user JSON of |
|                       |                       | the owner of the      |
|                       |                       | asset.                |
+-----------------------+-----------------------+-----------------------+
| datecreated           | string                | The date the folder   |
|                       |                       | was created.          |
+-----------------------+-----------------------+-----------------------+
| passwordprotected     | boolean               |                       |
+-----------------------+-----------------------+-----------------------+
| numassets             | integer               | How many assets are   |
|                       |                       | in the folder.        |
+-----------------------+-----------------------+-----------------------+
| numchildren           | integer               | How many nested       |
|                       |                       | folders are in the    |
|                       |                       | folder.               |
+-----------------------+-----------------------+-----------------------+
| clientfolderid        | string                | An optional           |
|                       |                       | identifier guaranteed |
|                       |                       | to be unique. This    |
|                       |                       | must be unique across |
|                       |                       | all folders a         |
|                       |                       | customer.             |
+-----------------------+-----------------------+-----------------------+
| permissions           | array                 | Actions available on  |
|                       |                       | folder and it's       |
|                       |                       | assets. assets:       |
|                       |                       | (view, upload,        |
|                       |                       | download, edit, move, |
|                       |                       | delete) folders:      |
|                       |                       | (view, create,        |
|                       |                       | download, edit, move, |
|                       |                       | delete)               |
+-----------------------+-----------------------+-----------------------+
| properties            | array                 | Folder properties     |
+-----------------------+-----------------------+-----------------------+

Folder properties

+----------------------------+-------------------------------------+
| Properties                 | Description                         |
+============================+=====================================+
| ALBWATERMARKPHOTOS         | Watermark assets in this folder     |
+----------------------------+-------------------------------------+
| ALBDISPLAYOWNERIMA         | Display asset owner                 |
+----------------------------+-------------------------------------+
| ALBEMAILHIRESDOWNLOAD      | Allow email high res downloads      |
+----------------------------+-------------------------------------+
| ALBENABLE_REQUESTRECIPIENT | Download request recipient          |
+----------------------------+-------------------------------------+
| ALBENABLE_REQUESTDOWNLOAD  | Allow download requests             |
+----------------------------+-------------------------------------+
| ALBENABLE_DOWNLOADUSAGE    | Require completion of download form |
+----------------------------+-------------------------------------+

.. _gettoplevelfolders:

View top level folders
~~~~~~~~~~~~~~~~~~~~~~

``GET /folders`` or ``GET /folders/0``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| thumbnail_ttl         | string                | Time to live for      |
|                       |                       | thumbnails            |
|                       |                       | Default: Set by the   |
|                       |                       | account admin         |
|                       |                       | Values: '+3 min',     |
|                       |                       | '+15 min', '+2        |
|                       |                       | hours', '+1 day', '+2 |
|                       |                       | weeks',               |
|                       |                       | 'no-expiration'       |
+-----------------------+-----------------------+-----------------------+

Curl

``curl https://apiv2.webdamdb.com/folders``

Example Response

``Status: 200 OK``

.. note:: Returns top level children.

.. code:: json

  [{
        "type": "folder",
        "id": "90672",
        "metadatatemplateid": null,
        "parent": "0",
        "name": "Marketing",
        "status": "active",
        "datecreated": "2011-09-23 13:17:48",
        "passwordprotected": "false",
        "numassets": "144",
        "numchildren": 1,
        "permissions": {
              "folders": [
                    "create",
                    "move",
                    "delete",
                    "edit"
              ],
              "assets": [
                    "download",
                    "upload",
                    "move",
                    "edit",
                    "delete"
              ]
        },
        "properties": {
              "ALBWATERMARKPHOTOS": "1",
              "ALBEMAILHIRESDOWNLOAD": "1",
              "ALBENABLE_REQUESTDOWNLOAD": "1",
              "ALBENABLE_REQUESTRECIPIENT": "admin"
        },
        "thumbnailurls": [{
              "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_0UerYozlI3.jpg"
        }, {
              "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_0UerYozlI3.jpg"
        }, {
              "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_0UerYozlI3.jpg"
        }, {
              "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_0UerYozlI3.jpg"
        }],
        "user": {
              "type": "user",
              "id": "9750",
              "email": "jsmith@example.com",
              "name": "John Smith",
              "username": "myusername"
        },
        "folders": [{
              "type": "folder",
              "id": "90674",
              "metadatatemplateid": null,
              "parent": "90672",
              "name": "Demo",
              "status": "active",
              "datecreated": "2011-09-23 13:17:48",
              "passwordprotected": "false",
              "numassets": "144",
              "numchildren": 0,
              "permissions": {
                    "folders": [
                          "create",
                          "move",
                          "delete",
                          "edit"
                    ],
                    "assets": [
                          "download",
                          "upload",
                          "move",
                          "edit",
                          "delete"
                    ]
              },
              "properties": {
                    "ALBWATERMARKPHOTOS": "1",
                    "ALBEMAILHIRESDOWNLOAD": "1",
                    "ALBENABLE_REQUESTDOWNLOAD": "1",
                    "ALBENABLE_REQUESTRECIPIENT": "admin"
              },
              "thumbnailurls": [{
                    "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_0UerYozlI4.jpg"
              }, {
                    "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_0UerYozlI4.jpg"
              }, {
                    "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_0UerYozlI4.jpg"
              }, {
                    "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_0UerYozlI4.jpg"
              }],
              "user": {
                    "type": "user",
                    "id": "9750",
                    "email": "jsmith@example.com",
                    "name": "John Smith",
                    "username": "myusername"
              }
        }]
  }, {
        "type": "folder",
        "id": "90786",
        "metadatatemplateid": null,
        "parent": "0",
        "name": "Sales",
        "status": "active",
        "datecreated": "2012-12-02 09:30:45",
        "passwordprotected": "false",
        "numassets": "10",
        "numchildren": 0,
        "permissions": {
              "folders": [
                    "create",
                    "move",
                    "delete",
                    "edit"
              ],
              "assets": [
                    "download",
                    "upload",
                    "move",
                    "edit",
                    "delete"
              ]
        },
        "properties": [],
        "thumbnailurls": [{
              "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_0UerYozlI3.jpg"
        }, {
              "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_0UerYozlI3.jpg"
        }, {
              "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_0UerYozlI3.jpg"
        }, {
              "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_0UerYozlI3.jpg"
        }],
        "user": {
              "type": "user",
              "id": "9750",
              "email": "jsmith@example.com",
              "name": "John Smith",
              "username": "myusername"
        }
  }]

Get folder information

``GET /folders/:folderid``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| thumbnail_ttl         | string                | Time to live for      |
|                       |                       | thumbnails            |
|                       |                       | Default: Set by the   |
|                       |                       | account admin         |
|                       |                       | Values: '+3 min',     |
|                       |                       | '+15 min', '+2        |
|                       |                       | hours', '+1 day', '+2 |
|                       |                       | weeks',               |
|                       |                       | 'no-expiration'       |
+-----------------------+-----------------------+-----------------------+

Curl

``curl https://apiv2.webdamdb.com/folders/90672``

Example Response

``Status: 200 OK``

.. note:: Returns top level children. Also takes an optional parameter
          ``clientfolderid=true`` to treat the id using a clientfolderid.

.. code:: json

  {
      "type": "folder",
      "id": "90672",
      "metadatatemplateid": null,
      "parent": "0",
      "name": "Marketing",
      "status": "active",
      "datecreated": "2011-09-23 13:17:48",
      "passwordprotected": "false",
      "numassets": "144",
        "permissions": {
          "folders": [
            "create",
            "move",
            "delete",
            "edit"
          ],
          "assets": [
            "download",
            "upload",
            "move",
            "edit",
            "delete"
          ]
        },
        "thumbnailurls": [
          {
            "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_0UerYozlI3.jpg"
          },
          {
            "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_0UerYozlI3.jpg"
          },
          {
            "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_0UerYozlI3.jpg"
          },
          {
            "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_0UerYozlI3.jpg"
          }
        ],
      "numchildren": 0,
        "user": {
          "type": "user",
          "id": "9750",
          "email": "jsmith@example.com",
          "name": "John Smith",
          "username": "myusername"
        }
  }

.. _getmultifolder:

Get multiple folder information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``GET /folders/list?ids={ids}``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| thumbnail_ttl         | string                | Time to live for      |
|                       |                       | thumbnails            |
|                       |                       | Default: Set by the   |
|                       |                       | account admin         |
|                       |                       | Values: '+3 min',     |
|                       |                       | '+15 min', '+2        |
|                       |                       | hours', '+1 day', '+2 |
|                       |                       | weeks',               |
|                       |                       | 'no-expiration'       |
+-----------------------+-----------------------+-----------------------+

Curl

``curl https://apiv2.webdamdb.com/folders/list?ids=192498,192517``

Example Response

``Status: 200 OK``

.. note:: Does not return top level children.

.. _createfolder:

Create a folder
~~~~~~~~~~~~~~~

``POST /folders``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| thumbnail_ttl         | string                | Time to live for      |
|                       |                       | thumbnails            |
|                       |                       | Default: Set by the   |
|                       |                       | account admin         |
|                       |                       | Values: '+3 min',     |
|                       |                       | '+15 min', '+2        |
|                       |                       | hours', '+1 day', '+2 |
|                       |                       | weeks',               |
|                       |                       | 'no-expiration'       |
+-----------------------+-----------------------+-----------------------+

Curl

``curl https://apiv2.webdamdb.com/folders -d '{"parent":"90784","clientfolderid":null, "name":"Marketing","status":"active"}' -X POST``

The clientfolderid is an OPTIONAL unique attribute on a folder that
enforces uniqueness across all folders. If there is a conflict on
uniqueness, a 403 HTTP response code will be issued.

Example Response

``Status: 201 Created``

.. code:: json

  {
      "type": "folder",
      "id": "90672",
      "metadatatemplateid": null,
      "parent": "0",
      "name": "Marketing",
      "status": "active",
      "datecreated": "2011-09-23 13:17:48",
      "passwordprotected": "false",
      "numassets": "144",
        "permissions": {
          "folders": [
            "create",
            "move",
            "delete",
            "edit"
          ],
          "assets": [
            "download",
            "upload",
            "move",
            "edit",
            "delete"
          ]
        },
        "thumbnailurls": [
          {
            "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_0UerYozlI3.jpg"
          },
          {
            "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_0UerYozlI3.jpg"
          },
          {
            "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_0UerYozlI3.jpg"
          },
          {
            "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_0UerYozlI3.jpg"
          }
        ],
      "numchildren": 0,
        "user": {
          "type": "user",
          "id": "9750",
          "email": "jsmith@example.com",
          "name": "John Smith",
          "username": "myusername"
        }
  }

.. _editfolder:

Edit a folder
~~~~~~~~~~~~~

``PUT /folders/:folderid``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| thumbnail_ttl         | string                | Time to live for      |
|                       |                       | thumbnails            |
|                       |                       | Default: Set by the   |
|                       |                       | account admin         |
|                       |                       | Values: '+3 min',     |
|                       |                       | '+15 min', '+2        |
|                       |                       | hours', '+1 day', '+2 |
|                       |                       | weeks',               |
|                       |                       | 'no-expiration'       |
+-----------------------+-----------------------+-----------------------+
| clientfolderid        | boolean               | An optional parameter |
|                       |                       | used to flag the      |
|                       |                       | :folderid to be       |
|                       |                       | treated as a client   |
|                       |                       | specified identifier. |
+-----------------------+-----------------------+-----------------------+

Curl

``curl https://apiv2.webdamdb.com/folders/90123 -d '{"name":"Marketing Asia","status":"active"}' -X PUT``

Example Response

``Status: 200 OK``

.. code:: json

  {
      "type": "folder",
      "id": "90672",
      "metadatatemplateid": null,
      "parent": "0",
      "name": "Marketing Asia",
      "status": "active",
      "datecreated": "2011-09-23 13:17:48",
      "passwordprotected": "false",
      "numassets": "144",
      "numchildren": 0,
        "permissions": {
          "folders": [
            "create",
            "move",
            "delete",
            "edit"
          ],
          "assets": [
            "download",
            "upload",
            "move",
            "edit",
            "delete"
          ]
        },
        "thumbnailurls": [
          {
            "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_0UerYozlI3.jpg"
          },
          {
            "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_0UerYozlI3.jpg"
          },
          {
            "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_0UerYozlI3.jpg"
          },
          {
            "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_0UerYozlI3.jpg"
          }
        ],
        "user": {
          "type": "user",
          "id": "9750",
          "email": "jsmith@example.com",
          "name": "John Smith",
          "username": "myusername"
        }
  }

.. _deletefolder:

Delete a folder
~~~~~~~~~~~~~~~

``DELETE /folders/:folderid``

Curl

``curl https://apiv2.webdamdb.com/folders/808232 -X DELETE``

Example Response

``Status: 204 OK``

.. _getfolderassets:

List assets for a folder
~~~~~~~~~~~~~~~~~~~~~~~~

``GET /folders/:folderid/assets``

Curl

``curl https://apiv2.webdamdb.com/folders/808232/assets sortby=filename&sortdir=desc&limit=20&offset=0``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| sortby                | string                | The field to sort by. |
|                       |                       | Possible values are   |
|                       |                       | filename, filesize,   |
|                       |                       | datecreated and       |
|                       |                       | datemodified.         |
|                       |                       | (Default=datecreated) |
+-----------------------+-----------------------+-----------------------+
| sortdir               | string                | The direction to sort |
|                       |                       | by. Possible values   |
|                       |                       | are asc or desc.      |
|                       |                       | (Default=asc)         |
+-----------------------+-----------------------+-----------------------+
| limit                 | integer               | The number of items   |
|                       |                       | to return.            |
|                       |                       | (Default=50,          |
|                       |                       | Maximum=100)          |
+-----------------------+-----------------------+-----------------------+
| offset                | integer               | The item number to    |
|                       |                       | start with. Default   |
|                       |                       | is 0.                 |
+-----------------------+-----------------------+-----------------------+
| types                 | string                | The file type filters |
|                       |                       | (Available filters:   |
|                       |                       | image, audiovideo,    |
|                       |                       | document,             |
|                       |                       | presentation, other)  |
+-----------------------+-----------------------+-----------------------+
| clientfolderid        | boolean               | An optional parameter |
|                       |                       | used to flag the      |
|                       |                       | :folderid should be   |
|                       |                       | treated as a client   |
|                       |                       | specified identifier. |
+-----------------------+-----------------------+-----------------------+

Example Response

``Status: 200 OK``

.. code:: json

  {
    "total_count": "1",
    "offset": 0,
    "limit": "50",
    "facets": {
      "types": {
        "image": "6",
        "document": "1",
        "audiovideo": "1",
        "presentation": "3",
        "other": null
      }
    },
    "items": [
      {
        "type": "asset",
        "id": "3456621",
        "status": "active",
        "filename": "Lightbox_switch.jpg",
        "name": "Lightbox_switch.jpg",
        "filesize": "0.17",
        "width": "890",
        "height": "748",
        "description": "",
        "filetype": "jpg",
        "colorspace": "RGB",
        "version": "1",
        "datecreated": "2013-07-10 14:30:25",
        "datemodified": "2013-07-10 14:30:25",
        "thumbnailurls": {
          { "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_9wFXFzBwv6.jpg" },
          { "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_9wFXFzBwv6.jpg" },
          { "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_9wFXFzBwv6.jpg" },
          { "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_9wFXFzBwv6.jpg" },
          { "size": "550", "url": "http://subdomain.webdamdb.com/image_dir/album90922/md_9wFXFzBwv6.jpg" }
        },
        "folder": {
          "type": "folder",
          "id": "90922",
          "name": "WORKS22"
        },
        "user": {
          "type": "user",
          "id": "9750",
          "email": "jsmith@example.com",
          "name": "John Smith",
          "username": "myusername"
        }
      }
    ]
  }

.. _assets-1:

Assets
------

.. _assetjson:

Asset JSON Format
~~~~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Attribute             | Type                  | Description           |
+=======================+=======================+=======================+
| type                  | string                | This is equal to      |
|                       |                       | "asset".              |
+-----------------------+-----------------------+-----------------------+
| id                    | long                  | The unique id of the  |
|                       |                       | asset.                |
+-----------------------+-----------------------+-----------------------+
| status                | string                | The current state of  |
|                       |                       | the asset, either     |
|                       |                       | active or inactive.   |
+-----------------------+-----------------------+-----------------------+
| filename              | string                | The filename of the   |
|                       |                       | asset.                |
+-----------------------+-----------------------+-----------------------+
| version               | string                | The version number of |
|                       |                       | the file. Default is  |
|                       |                       | 1.                    |
+-----------------------+-----------------------+-----------------------+
| name                  | string                | The name of the       |
|                       |                       | asset.                |
+-----------------------+-----------------------+-----------------------+
| filesize              | string                | The size of the asset |
|                       |                       | in bytes.             |
+-----------------------+-----------------------+-----------------------+
| width                 | long                  | The width in pixels   |
|                       |                       | of the asset. The     |
|                       |                       | width attribute only  |
|                       |                       | applies to certain    |
|                       |                       | types of assets such  |
|                       |                       | as image or videos.   |
+-----------------------+-----------------------+-----------------------+
| height                | long                  | The height in pixels  |
|                       |                       | of the asset. The     |
|                       |                       | height attribute only |
|                       |                       | applies to certain    |
|                       |                       | types of assets such  |
|                       |                       | as image or videos.   |
+-----------------------+-----------------------+-----------------------+
| filetype              | string                | The type of file.     |
+-----------------------+-----------------------+-----------------------+
| colorspace            | string                | The colorspace of the |
|                       |                       | asset. This attribute |
|                       |                       | only applies to       |
|                       |                       | certain types of      |
|                       |                       | assets such as image. |
+-----------------------+-----------------------+-----------------------+
| thumbnailurls         | array                 | The link to thumbnail |
|                       |                       | of the asset.         |
|                       |                       | Available max         |
|                       |                       | dimension are 100px,  |
|                       |                       | 150px, 220px, 310px   |
|                       |                       | and 550px. This       |
|                       |                       | attribute only        |
|                       |                       | applies to certain    |
|                       |                       | types of assets such  |
|                       |                       | as image or videos.   |
+-----------------------+-----------------------+-----------------------+
| datecreated           | string                | The unix timestamp of |
|                       |                       | the date the asset    |
|                       |                       | was created or        |
|                       |                       | uploaded.             |
+-----------------------+-----------------------+-----------------------+
| datemodified          | string                | The unix timestamp of |
|                       |                       | the date the asset    |
|                       |                       | was last modified.    |
+-----------------------+-----------------------+-----------------------+
| datecaptured          | string                | The unix timestamp of |
|                       |                       | the date the asset    |
|                       |                       | was captured. This    |
|                       |                       | usually only applies  |
|                       |                       | to files generated by |
|                       |                       | a camera or scanned   |
|                       |                       | in.                   |
+-----------------------+-----------------------+-----------------------+
| numComments           | integer               | The number of         |
|                       |                       | comments on this      |
|                       |                       | asset.                |
+-----------------------+-----------------------+-----------------------+
| user                  | Mini user             | The mini user JSON of |
|                       |                       | the owner of the      |
|                       |                       | asset.                |
+-----------------------+-----------------------+-----------------------+
| folder                | Mini folder           | The mini folder JSON  |
|                       |                       | the asset is located  |
|                       |                       | in.                   |
+-----------------------+-----------------------+-----------------------+

.. _getasset:

Get asset information
~~~~~~~~~~~~~~~~~~~~~

``GET /assets/:assetid``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| thumbnail_ttl         | string                | Time to live for      |
|                       |                       | thumbnails            |
|                       |                       | Default: Set by the   |
|                       |                       | account admin         |
|                       |                       | Values: '+3 min',     |
|                       |                       | '+15 min', '+2        |
|                       |                       | hours', '+1 day', '+2 |
|                       |                       | weeks',               |
|                       |                       | 'no-expiration'       |
+-----------------------+-----------------------+-----------------------+

Curl

``curl https://apiv2.webdamdb.com/assets/23422``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "type": "asset",
    "id": "3455969",
    "status": "active",
    "filename": "XAAAZZZZZ.jpg",
    "name": "Micro turbine 60",
    "filesize": "0.07",
    "width": "647",
    "height": "433",
    "description": "micro-turbine, 60- or 100-kilowatt wind turbines",
    "filetype": "jpg",
    "colorspace": "RGB",
    "version": "4",
    "datecreated": "2012-12-13 13:50:10",
    "datemodified": "2013-08-17 14:44:15",
    "thumbnailurls": {
      { "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_0UerYozlI3.jpg" },
      { "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_0UerYozlI3.jpg" },
      { "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_0UerYozlI3.jpg" },
      { "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_0UerYozlI3.jpg" },
      { "size": "550", "url": "http://subdomain.webdamdb.com/s/md_0UerYozlI3.jpg" }
    },
    "folder": {
      "type": "folder",
      "id": "90754",
      "name": "Jody's New Folder - Don't Touch"
    },
    "user": {
      "type": "user",
      "id": "9750",
      "email": "jsmith@example.com",
      "name": "John Smith",
      "username": "myusername"
    }
  }

Get multiple asset information

``GET /assets/list?ids={ids}``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| thumbnail_ttl         | string                | Time to live for      |
|                       |                       | thumbnails            |
|                       |                       | Default: Set by the   |
|                       |                       | account admin         |
|                       |                       | Values: '+3 min',     |
|                       |                       | '+15 min', '+2        |
|                       |                       | hours', '+1 day', '+2 |
|                       |                       | weeks',               |
|                       |                       | 'no-expiration'       |
+-----------------------+-----------------------+-----------------------+

Curl

``curl https://apiv2.webdamdb.com/assets/list?ids=5992827,5992826``

Example Response

``Status: 200 OK``

.. _editasset:

Edit an asset
~~~~~~~~~~~~~

``PUT /assets/:assetid``

If an asset is uploaded and its required fields are not filled in, the
asset is in onhold status and cannot be activated until all required
fields are supplied. Any attempt to change the status to 'active' for
assets that still require metadata will return back 409.

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| filename              | string                | The new filename for  |
|                       |                       | the asset.            |
+-----------------------+-----------------------+-----------------------+
| status                | string                | The new status of the |
|                       |                       | asset. Either active  |
|                       |                       | or inactive.          |
+-----------------------+-----------------------+-----------------------+
| name                  | string                | The new name for the  |
|                       |                       | asset.                |
+-----------------------+-----------------------+-----------------------+
| description           | string                | The new description   |
|                       |                       | of the asset.         |
+-----------------------+-----------------------+-----------------------+
| folder                | long                  | The id of the folder  |
|                       |                       | to move asset to.     |
+-----------------------+-----------------------+-----------------------+
| thumbnail_ttl         | string                | Time to live for      |
|                       |                       | thumbnails            |
|                       |                       | Default: Set by the   |
|                       |                       | account admin         |
|                       |                       | Values: '+3 min',     |
|                       |                       | '+15 min', '+2        |
|                       |                       | hours', '+1 day', '+2 |
|                       |                       | weeks',               |
|                       |                       | 'no-expiration'       |
+-----------------------+-----------------------+-----------------------+

Curl

``curl https://apiv2.webdamdb.com/assets/23422 -d '{"status": "active", "filename": "newfilename.jpg", "description": "Nice", "folder": { "id": "90751" }}'``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "type": "asset",
    "id": "3455969",
    "status": "active",
    "filename": "XAAAZZZZZ.jpg",
    "name": "Micro turbine 60",
    "filesize": "0.07",
    "width": "647",
    "height": "433",
    "description": "micro-turbine, 60- or 100-kilowatt wind turbines",
    "filetype": "jpg",
    "colorspace": "RGB",
    "version": "4",
    "datecreated": "2012-12-13 13:50:10",
    "datemodified": "2013-08-17 14:44:15",
    "thumbnailurls": {
      { "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_0UerYozlI3.jpg" },
      { "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_0UerYozlI3.jpg" },
      { "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_0UerYozlI3.jpg" },
      { "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_0UerYozlI3.jpg" },
      { "size": "550", "url": "http://subdomain.webdamdb.com/s/md_0UerYozlI3.jpg" }
    },
    "folder": {
      "type": "folder",
      "id": "90754",
      "name": "Jody's New Folder - Don't Touch"
    },
    "user": {
      "type": "user",
      "id": "9750",
      "email": "jsmith@example.com",
      "name": "John Smith",
      "username": "myusername"
    }
  }

.. _deleteasset:

Delete an asset
~~~~~~~~~~~~~~~

``DELETE /assets/:assetid``

Curl

``curl https://apiv2.webdamdb.com/assets/23422 -X DELETE``

Example Response

``Status: 204 OK``

.. _uploadasset:

Upload an asset (optimized)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This API endpoint is a 3-step process which provides the following
advantages over the deprecated method:

-  Faster upload speeds by leveraging AWS S3
-  Support for files up to 5 gigabytes.

This API endpoint only supports upload up to 5 GB in size.

#. | ``GET /awss3/generateupload?filesize=:filesize&folderid=:folderid&filename=:filename&contenttype=:contenttype&assetid=:assetid&intent=:intent``
   | Returns a JSON response that contains:

   #. a presigned url (:presignedurl) valid for 5 minutes
   #. the process id (:processid) for the upload.

   Requirements:

   -  :filesize = size of the file in bytes (e.g. 1000000)
   -  :folderid = The target numeric folder id for this asset to reside
      in (e.g. 1366416)
   -  :filename = A utf8 url-encoded filename of the asset (e.g.
      shutterstock.jpg)
   -  :contenttype = The mime type of the asset (e.g. image/jpeg)
   -  :assetid = An OPTIONAL assetid that indicates this is an update.
      If not supplied, is treated as a new asset.
   -  :intent = Optional, used in conjunction with the :assetid to
      signal intention. Valid values are "newversion" or "replace".
      Default value is "replace".

   Curl

   ``curl "http://apiv2.webdamdb.com/ws/awss3/generateupload?filesize=1000000&folderid=1366416&filename=shutterstock.jpg&contenttype=image/jpeg"``

   Example Response

   ``Status: 200 OK``

  .. code:: json

    {
        "presignedUrl": "https://webdamuploads.s3.amazonaws.com/12722_7c74b491_2be1_4f4f_b215_b5533f4cd25e.jpg?AWSAccessKeyId=ABCDEFG&Expires=1471294558&Signature=E6vZtQBHTvfcRWdqwzWt65UrxX8%3D",
        "processId": "57165496"
    }

#. | ``PUT :presignedurl``
   | Upload the file directly to AWS S3.
   | Requirements:

   -  :presignedurl = A valid presigned URL from Step 1
   -  Content-Type header = A content type header matching the
      contenttype from Step 1 MUST be provided as part of the PUT.

   Curl

   ``curl -H 'Content-Type: image/jpeg' -T shutterstock.jpg "https://webdamuploads.s3.amazonaws.com/12722_7c74b491_2be1_4f4f_b215_b5533f4cd25e.jpg?AWSAccessKeyId=ABCDEFG&Expires=1471294558&Signature=E6vZtQBHTvfcRWdqwzWt65UrxX8%3D"``

   Example Response

   ``Status: 100 Continue``

   ``* We are completely uploaded and fine``

#. | ``PUT http://apiv2.webdamdb.com/ws/awss3/finishupload/:processid``
   | Signal to |acquia-product:dam| that the upload has completed and
     ready for thumbnailing. Returns back the inserted or updated asset
     id.
   | Requirements:

   -  :processid = The numeric process id returned from Step 1

   Curl

   ``curl -X PUT "https://apiv2.webdamdb.com/ws/awss3/finishupload/57165494"``

   Example Response

   ``Status: 200 OK``

   .. code:: json

      {
          "id": "1234567"
      }

.. _downloadasset:

Download an asset
~~~~~~~~~~~~~~~~~

``GET /assets/:id/download``

Optional query parameters

-  sendNotificationsOff = valid values are 1 or 0, used to
   programmatically disable triggering notifications. Default is set to
   be 0.
-  trackDownloadsOff = valid values are 1 or 0, used to programmatically
   disable triggering download tracking. Default is set to be 0.
-  geturl = valid values are 1 or 0, used to return back a json payload
   with the url if enabled, otherwise serve the asset contents. The
   presigned url is valid only for 60 seconds. Default is set to 0.

Curl

``curl -L https://apiv2.webdamdb.com/assets/123123123/download``

Example Response

``Status: 200 OK``

``RAW FILE CONTENTS``

.. _viewassetversions:

View versions of an asset
~~~~~~~~~~~~~~~~~~~~~~~~~

``GET /assets/:assetid/versions``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| thumbnail_ttl         | string                | Time to live for      |
|                       |                       | thumbnails            |
|                       |                       | Default: Set by the   |
|                       |                       | account admin         |
|                       |                       | Values: '+3 min',     |
|                       |                       | '+15 min', '+2        |
|                       |                       | hours', '+1 day', '+2 |
|                       |                       | weeks',               |
|                       |                       | 'no-expiration'       |
+-----------------------+-----------------------+-----------------------+

Curl

``curl https://apiv2.webdamdb.com/assets/7812323/versions``

Example Response

``Status: 200 OK``

.. code:: json

  [
    {
      "type": "assetversion",
      "id": "3455969",
      "status": "inactive",
      "filename": "aaz.jpg",
      "name": "aaz.jpg",
      "filesize": "3.26",
      "width": "3040",
      "height": "2908",
      "description": "This facility, which is the only of its kind, tests how distributed generation sources connect and work together. At the facility, generation sources such as a 30-kilowatt micro-turbine, 60- or 100-kilowatt wind turbines, various sized diesel generators, ",
      "filetype": "jpg",
      "colorspace": "RGB",
      "version": "1",
      "datecreated": "2012-12-13 13:50:10",
      "datemodified": "2013-01-03 13:22:22",
      "thumbnailurls": {
        { "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_.jpg" },
        { "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_.jpg" },
        { "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_.jpg" },
        { "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_.jpg" },
        { "size": "550", "url": "http://subdomain.webdamdb.com/image_dir/album90784/md_aaz.jpg.mp4.jpg" }
      },
      "folder": {
        "type": "folder",
        "id": "90784",
        "name": "Videos"
      }
    },
    {
      "type": "assetversion",
      "id": "3455969",
      "status": "active",
      "filename": "ZIPJJSSS 1BR1.jpg",
      "name": "aaz.jpg",
      "filesize": "0.07",
      "width": "647",
      "height": "433",
      "description": "This facility, which is the only of its kind, tests how distributed generation sources connect and work together. At the facility, generation sources such as a 30-kilowatt micro-turbine, 60- or 100-kilowatt wind turbines, various sized diesel generators, ",
      "filetype": "jpg",
      "colorspace": "RGB",
      "version": "2",
      "datecreated": "2012-12-13 13:50:10",
      "datemodified": "2013-01-05 14:35:07",
      "thumbnailurls": {
        { "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_ZIPJJSSS.jpg" },
        { "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_ZIPJJSSS.jpg" },
        { "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_ZIPJJSSS.jpg" },
        { "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_ZIPJJSSS.jpg" },
        { "size": "550", "url": "http://subdomain.webdamdb.com/image_dir/album90784/md_ZIPJJSSS.jpg" }
      },
      "folder": {
        "type": "folder",
        "id": "90784",
        "name": "Videos"
      }
    },
    {
      "type": "assetversion",
      "id": "3455969",
      "status": "active",
      "filename": "ZIPJJSSS 1BR2.jpg",
      "name": "aaz.jpg",
      "filesize": "0.08",
      "width": "650",
      "height": "433",
      "description": "This facility, which is the only of its kind, tests how distributed generation sources connect and work together. At the facility, generation sources such as a 30-kilowatt micro-turbine, 60- or 100-kilowatt wind turbines, various sized diesel generators, ",
      "filetype": "jpg",
      "colorspace": "RGB",
      "version": "3",
      "datecreated": "2012-12-13 13:50:10",
      "datemodified": "2013-01-05 14:43:21",
      "thumbnailurls": {
        { "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_ZIPJJSSS.jpg" },
        { "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_ZIPJJSSS.jpg" },
        { "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_ZIPJJSSS.jpg" },
        { "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_ZIPJJSSS.jpg" },
        { "size": "550", "url": "http://subdomain.webdamdb.com/image_dir/album90784/md_ZIPJJSSS.jpg" }
      },
      "folder": {
        "type": "folder",
        "id": "90784",
        "name": "Videos"
      }
    }
  ]

.. _getassetversion:

Get an asset version
~~~~~~~~~~~~~~~~~~~~

``GET /assets/:assetid/versions/:version``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| thumbnail_ttl         | string                | Time to live for      |
|                       |                       | thumbnails            |
|                       |                       | Default: Set by the   |
|                       |                       | account admin         |
|                       |                       | Values: '+3 min',     |
|                       |                       | '+15 min', '+2        |
|                       |                       | hours', '+1 day', '+2 |
|                       |                       | weeks',               |
|                       |                       | 'no-expiration'       |
+-----------------------+-----------------------+-----------------------+

Curl

``curl https://apiv2.webdamdb.com/assets/7812323/versions/3``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "type": "assetversion",
    "id": "3455969",
    "status": "active",
    "filename": "XAAAZZZZZ.jpg",
    "name": "Micro turbine 60",
    "filesize": "0.07",
    "width": "647",
    "height": "433",
    "description": "micro-turbine, 60- or 100-kilowatt wind turbines",
    "filetype": "jpg",
    "colorspace": "RGB",
    "version": "3",
    "datecreated": "2012-12-13 13:50:10",
    "datemodified": "2013-08-17 14:44:15",
    "thumbnailurls": {
      { "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_0UerYozlI3.jpg" },
      { "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_0UerYozlI3.jpg" },
      { "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_0UerYozlI3.jpg" },
      { "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_0UerYozlI3.jpg" },
      { "size": "550", "url": "http://subdomain.webdamdb.com/s/md_0UerYozlI3.jpg" }
    },
    "folder": {
      "type": "folder",
      "id": "90754",
      "name": "Jody's New Folder - Don't Touch"
    },
    "user": {
      "type": "user",
      "id": "9750",
      "email": "jsmith@example.com",
      "name": "John Smith",
      "username": "myusername"
    }
  }

.. _deleteassetversion:

Delete an asset version
~~~~~~~~~~~~~~~~~~~~~~~

``DELETE /assets/:assetid/versions/:version``

Curl

``curl https://apiv2.webdamdb.com/assets/7812323/versions/3 -X DELETE``

Example Response

``Status: 204 OK``

.. _restoreassetversion:

Restore an asset version
~~~~~~~~~~~~~~~~~~~~~~~~

``POST /assets/:assetid/versions/:version``

Curl

``curl https://apiv2.webdamdb.com/assets/7812323/versions/3 -X POST``

Example Response

``Status: 204 OK``

.. _downloadassetversion:

Download an asset version
~~~~~~~~~~~~~~~~~~~~~~~~~

``GET /assets/:id/versions/:version/download``

Optional query parameters

-  sendNotificationsOff = valid values are 1 or 0, used to
   programmatically disable triggering notifications. Default is set to
   be 0.
-  trackDownloadsOff = valid values are 1 or 0, used to programmatically
   disable triggering download tracking. Default is set to be 0.
-  geturl = valid values are 1 or 0, used to return back a json payload
   with the url if enabled, otherwise serve the asset contents. The
   presigned url is valid only for 60 seconds. Default is set to 0.

Curl

``curl -L https://apiv2.webdamdb.com/assets/123123123/versions/3/download``

Example Response

``Status: 200 OK``

``RAW FILE CONTENTS``

.. _assetrelated:

Get related assets for an asset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``GET /assets/:assetid/related``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| thumbnail_ttl         | string                | Time to live for      |
|                       |                       | thumbnails            |
|                       |                       | Default: Set by the   |
|                       |                       | account admin         |
|                       |                       | Values: '+3 min',     |
|                       |                       | '+15 min', '+2        |
|                       |                       | hours', '+1 day', '+2 |
|                       |                       | weeks',               |
|                       |                       | 'no-expiration'       |
+-----------------------+-----------------------+-----------------------+

Curl

``curl https://apiv2.webdamdb.com/assets/13213/related``

Example Response

``Status: 200 OK``

.. code:: json

  [
    {
      "type": "asset",
      "id": "3456621",
      "status": "active",
      "filename": "Lightbox_switch.jpg",
      "name": "Lightbox_switch.jpg",
      "filesize": "0.17",
      "width": "890",
      "height": "748",
      "description": "",
      "filetype": "jpg",
      "colorspace": "RGB",
      "version": "1",
      "datecreated": "2013-07-10 14:30:25",
      "datemodified": "2013-07-10 14:30:25",
      "thumbnailurls": {
        { "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_9wFXFzBwv6.jpg" },
        { "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_9wFXFzBwv6.jpg" },
        { "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_9wFXFzBwv6.jpg" },
        { "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_9wFXFzBwv6.jpg" },
        { "size": "550", "url": "http://subdomain.webdamdb.com/image_dir/album90922/md_9wFXFzBwv6.jpg" }
      },
      "folder": {
        "type": "folder",
        "id": "90922",
        "name": "WORKS22"
      },
      "user": {
        "type": "user",
        "id": "9750",
        "email": "jsmith@example.com",
        "name": "John Smith",
        "username": "myusername"
      }
    }
  ]

.. _sendassetdownload:

Send asset download
~~~~~~~~~~~~~~~~~~~

``POST /assets/:assetid/senddownload``

Curl

``curl https://apiv2.webdamdb.com/assets/7812323/senddownload -d '{"emails":["userone@emaildomain.com","usertwo@emaildomain.com"], "subject": "Cool asset", "message": "Check out this cool asset", "expirationdate": "2013-12-07"}' -X POST``

Example Response

``Status: 200 OK``

.. code:: json

  {
      "downloadkey": "v6hHtXRwgAL9KkMj"
  }

.. _metadata-1:

Metadata
--------

.. _getassetxmp:

View asset XMP metadata
~~~~~~~~~~~~~~~~~~~~~~~

``GET /assets/:id/metadatas/xmp``

Curl

``curl https://apiv2.webdamdb.com/assets/2342322/metadatas/xmp``

Example Response

``Status: 200 OK``

``{     "type": "assetxmp",     "headline": "myasset",     "credit": "John Doe",     "countryname": "United States of America",     "keyword": "New York,Places,Ranula,San Francisco" }``

View list of assets XMP metadata

``https://apiv2.webdamdb.com/assets/2342322,5342344/metadatas/xmp``

.. note:: The limit is 50 assets.

.. _editassetxmp:

Edit asset XMP metadata
~~~~~~~~~~~~~~~~~~~~~~~

``PUT /assets/:id/metadatas/xmp``

Curl

``curl https://apiv2.webdamdb.com/assets/2342322/metadatas/xmp -d '{"keyword":"cat, dog, play together, not well"}' -X PUT``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "type": "assetxmp",
    "headline": "myasset",
    "credit": "John Doe",
    "countryname": "United States of America",
    "keyword": "cat, dog, play together, not well"
  }

Remove Keywords

``curl https://apiv2.webdamdb.com/assets/2342322/metadatas/xmp -d '{"keyword": "","replacekeywords": "true"}' -X PUT``

Disable Notifications

``curl https://apiv2.webdamdb.com/assets/2342322/metadatas/xmp -d '{"sendNotificationsOff": "1"}' -X PUT``

.. _getassetexif:

View asset EXIF metadata
~~~~~~~~~~~~~~~~~~~~~~~~

``GET /assets/:id/metadatas/exif``

Curl

``curl https://apiv2.webdamdb.com/assets/2342322/metadatas/exif``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "type": "assetexif",
    "ycbcrpositioning": "Centered",
    "resolutionunit": "inches",
    "yresolution": "300",
    "xresolution": "300"
  }

View list of assets EXIF metadata

``https://apiv2.webdamdb.com/assets/2342322,5342344/metadatas/exif``

.. note:: The limit is 50 assets.

.. _metadata-templates-1:

Metadata Templates
------------------

.. _lightboxjson:

Metadata Template JSON Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Attribute             | Type                  | Description           |
+=======================+=======================+=======================+
| id                    | long                  | The unique id of the  |
|                       |                       | metadata template.    |
+-----------------------+-----------------------+-----------------------+
| name                  | string                | The unique name of    |
|                       |                       | the metadata          |
|                       |                       | template.             |
+-----------------------+-----------------------+-----------------------+
| numFolders            | integer               | The number of folders |
|                       |                       | for which this        |
|                       |                       | metadata template     |
|                       |                       | applies.              |
+-----------------------+-----------------------+-----------------------+
| owner_id              | long                  | The unique id of the  |
|                       |                       | user who created the  |
|                       |                       | metadata template.    |
+-----------------------+-----------------------+-----------------------+
| values                | array                 | The list of metadata  |
|                       |                       | values that the       |
|                       |                       | metadata template     |
|                       |                       | consists of. Consists |
|                       |                       | of the "value" and    |
|                       |                       | "append", where       |
|                       |                       | "append": 1 to        |
|                       |                       | append, and "append": |
|                       |                       | 0 for replace.        |
|                       |                       | "Append" is always    |
|                       |                       | "replace" for         |
|                       |                       | "select" type         |
|                       |                       | metadata. For other   |
|                       |                       | metadata types,       |
|                       |                       | "append" is required. |
+-----------------------+-----------------------+-----------------------+

.. _getmetadatatemplates:

Get all metadata templates
~~~~~~~~~~~~~~~~~~~~~~~~~~

``GET /metadatatemplates``

Curl

``curl https://apiv2.webdamdb.com/metadatatemplates``

Example Response

``Status: 200 OK``

.. code:: json

  [
    {
      "id": "2216",
      "name": "My Template",
      "numFolders": 3,
      "folderids" : [ "123", "456", "789"],
      "owner_id": "9750"
    }
  ]

.. _getmetadatatemplate:

Get a metadata template
~~~~~~~~~~~~~~~~~~~~~~~

``GET /metadatatemplates/:templateid``

Curl

``curl https://apiv2.webdamdb.com/metadatatemplates/2216``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "id": "2216",
    "name": "My Template",
    "folderids": [ "123", "456", "789" ],
    "values": {
      "OBJECTNAME": {
        "value": "Sample object name",
        "append": "1"
      },
      "CREDIT": {
        "value": "Sample credit",
        "append": "0"
      },
      "CAPTION": {
        "value": "Sample caption",
        "append": "0"
      }
    }
  }

.. _createmetadatatemplate:

Create a metadata template
~~~~~~~~~~~~~~~~~~~~~~~~~~

``POST /metadatatemplates``

Curl

``curl https://apiv2.webdamdb.com/metadatatemplates -d '{"name":"New Template","values":{"CREDIT":{"value":"Some credit","append":"1"},"CAPTION":{"value":"Some caption","append":"0"},"CITY":{"value":"Some city","append":"0"}}}' -X POST``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "id": "2217",
    "name": "New Template",
    "folderids": [],
    "values": {
      "CREDIT": {
        "value": "Some credit",
        "append": "1"
      },
      "CAPTION": {
        "value": "Some caption",
        "append": "0"
      },
      "CITY": {
        "value": "Some city",
        "append": "0"
      }
    }
  }

.. _editmetadatatemplate:

Edit a metadata template
~~~~~~~~~~~~~~~~~~~~~~~~

``PUT /metadatatemplates/:templateid``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| name                  | string                | The new name for the  |
|                       |                       | template. Optional,   |
|                       |                       | but either "name" or  |
|                       |                       | "values" must be      |
|                       |                       | passed in.            |
+-----------------------+-----------------------+-----------------------+
| replace               | integer               | Either 1 (replace     |
|                       |                       | current template with |
|                       |                       | these new values) or  |
|                       |                       | 0 (only change the    |
|                       |                       | metadata that was     |
|                       |                       | passed in). Required. |
+-----------------------+-----------------------+-----------------------+
| values                | array                 | The metadatas to be   |
|                       |                       | updated in the        |
|                       |                       | template. Optional,   |
|                       |                       | but either "name" or  |
|                       |                       | "values" must be      |
|                       |                       | passed in.            |
+-----------------------+-----------------------+-----------------------+

"Values" Sub-parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| value                 | array                 | The new value for the |
|                       |                       | metadata field. If a  |
|                       |                       | multi-select          |
|                       |                       | picklist, can be an   |
|                       |                       | array of string       |
|                       |                       | values.               |
+-----------------------+-----------------------+-----------------------+
| append                | integer               | Can be 1 or 0. Refers |
|                       |                       | to whether this       |
|                       |                       | metadata will act as  |
|                       |                       | an appended or        |
|                       |                       | replaced value to new |
|                       |                       | assets in the folder  |
|                       |                       | this template applies |
|                       |                       | to. Does not affect   |
|                       |                       | single-select         |
|                       |                       | picklist metadata     |
|                       |                       | fields, and required  |
|                       |                       | for other metadata    |
|                       |                       | field types.          |
+-----------------------+-----------------------+-----------------------+
| replace               | integer               | Required parameter    |
|                       |                       | for multi-select      |
|                       |                       | picklists. Can be     |
|                       |                       | 0-3. 0 means          |
|                       |                       | comma-separated       |
|                       |                       | values will be        |
|                       |                       | appended to existing  |
|                       |                       | picklist values (no   |
|                       |                       | duplicates accepted). |
|                       |                       | 1 is total-replace. 2 |
|                       |                       | is to delete the new  |
|                       |                       | values from the       |
|                       |                       | existing values       |
|                       |                       | (values must already  |
|                       |                       | exist). 3 requires an |
|                       |                       | associative object    |
|                       |                       | where existing key    |
|                       |                       | replaces new value    |
|                       |                       | (requires format:     |
|                       |                       | values: {"Search for  |
|                       |                       | value":"Replace with  |
|                       |                       | value"} and replaces  |
|                       |                       | in the order that     |
|                       |                       | they are received.    |
+-----------------------+-----------------------+-----------------------+

Curl

``curl https://apiv2.webdamdb.com/metadatatemplates/2217 -d '{"name":"New Template Name","replace":0,"values":{"CREDIT":{"value":"Credit 1, Credit 2, Credit 3","append":"0","replace":0},"CAPTION":{"value":"Some caption","append":"0"},"OBJECTNAME":{"value":"Some object name","append":"1"}}}' -X PUT``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "id": "2217",
    "name": "New Template Name",
    "folderids": ["123", "456", "789"],
    "values": {
      "CREDIT": {
        "value": "Credit 0, Credit 1, Credit 2, Credit 3"",
        "append": "0"
      },
      "CAPTION": {
        "value": "Some caption",
        "append": "0"
      },
      "OBJECTNAME": {
        "value": "Some object name",
        "append": "1"
      }
    }
  }

.. _deletemetadatatemplate:

Delete a metadata template
~~~~~~~~~~~~~~~~~~~~~~~~~~

``DELETE /metadatatemplates/:templateid``

Curl

``curl https://apiv2.webdamdb.com/metadatatemplates/2217 -X DELETE``

Example Response

``Status: 200 OK``

.. _applymetadatatemplate:

Apply a metadata template to folders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``POST /metadatatemplates/:templateid/apply``

Curl

``curl https://apiv2.webdamdb.com/metadatatemplates/2216/apply -d '{"folders":[{"id":"90672","state":1}]}' -X POST``

Example Response

``Status: 200 OK``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| folders               | array                 | The folders to        |
|                       |                       | apply/remove the      |
|                       |                       | metadata template     |
|                       |                       | to/from. Each folder  |
|                       |                       | object must contain:  |
|                       |                       |                       |
|                       |                       | -  id - (long) The    |
|                       |                       |    unique id of the   |
|                       |                       |    folder.            |
|                       |                       | -  state - (integer)  |
|                       |                       |    The state of the   |
|                       |                       |    action. Available  |
|                       |                       |    states: 1 (apply)  |
|                       |                       |    and 0 (remove).    |
+-----------------------+-----------------------+-----------------------+

.. _metadata-schema-1:

Metadata Schema
---------------

.. _metadata-schema-json:

Metadata Schema JSON Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Attribute             | Type                  | Description           |
+=======================+=======================+=======================+
| field                 | string                | The unique            |
|                       |                       | field/metadata code.  |
+-----------------------+-----------------------+-----------------------+
| name                  | string                | The name of the       |
|                       |                       | metadata field.       |
+-----------------------+-----------------------+-----------------------+
| label                 | string                | The label of the      |
|                       |                       | metadata field.       |
+-----------------------+-----------------------+-----------------------+
| status                | string                | Whether or not this   |
|                       |                       | metadata is part of   |
|                       |                       | the active schema.    |
|                       |                       | Either "active" or    |
|                       |                       | "inactive".           |
+-----------------------+-----------------------+-----------------------+
| searchable            | string                | Whether or not this   |
|                       |                       | metadata can be       |
|                       |                       | searched upon. Either |
|                       |                       | "yes" or "no".        |
+-----------------------+-----------------------+-----------------------+
| position              | string                | Numeric string        |
|                       |                       | containing the        |
|                       |                       | position of this      |
|                       |                       | metadata field in the |
|                       |                       | schema.               |
+-----------------------+-----------------------+-----------------------+
| values                | array                 | Array of values that  |
|                       |                       | gets returned only if |
|                       |                       | "full" parameter is   |
|                       |                       | passed into the GET   |
|                       |                       | request. Returns only |
|                       |                       | if "type" is "select" |
|                       |                       | or "multiselect".     |
+-----------------------+-----------------------+-----------------------+
| type                  | string                | Type of the metadata  |
|                       |                       | in the schema that    |
|                       |                       | gets returned only if |
|                       |                       | "full" parameter is   |
|                       |                       | passed into the GET   |
|                       |                       | request. Returns:     |
|                       |                       | "text", "textarea",   |
|                       |                       | "select", or          |
|                       |                       | "multiselect".        |
+-----------------------+-----------------------+-----------------------+

.. _getmetadataschema:

Get metadata schema
~~~~~~~~~~~~~~~~~~~

``GET /metadataschemas/xmp``

Curl

``curl https://apiv2.webdamdb.com/metadataschemas/xmp?full=1``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "xmpschema": [
      {
        "field": "CAPTION",
        "name": "Caption\/Abstract",
        "label": "Caption\/Description",
        "status": "active",
        "searchable": "yes",
        "position": "2",
        "type": "textarea"
      },
      {
        "field": "HEADLINE",
        "name": "Headline",
        "label": "Headline\/Name",
        "status": "active",
        "searchable": "yes",
        "position": "3",
        "values": [
          "Headline 1",
          "Headline 2",
          "Headline 3"
        ],
        "type": "select"
      },
      {
        "field": "SOURCE",
        "name": "Source",
        "label": "Source",
        "status": "active",
        "searchable": "yes",
        "position": "5",
        "values": [
          "Source 1",
          "Source 2",
          "Source 3"
        ],
        "type": "multiselect"
      },
      {
        "field": "BYLINE",
        "name": "By-line",
        "label": "Photographer",
        "status": "active",
        "searchable": "yes",
        "position": "8",
        "type": "text"
      }
    ]
  }

.. note:: Passing ?full=1 to GET /metadataschemas/xmp adds the "values" and "type"
          fields to the response.

.. _updatemetadatatype:

Update metadata type
~~~~~~~~~~~~~~~~~~~~

``POST /metadataschemas/xmp``

Curl

``curl https://apiv2.webdamdb.com/metadataschemas/xmp -d '[{"field":"HEADLINE", "sort":0, "multiselect":1, "values":["Headline 1","Headline 3","Headline 3"], "replace":1}, {"field":"CREDIT", "sort": 0, "multiselect":0, "values":["Credit 3"], "replace":2}, {"field":"SOURCE", "sort":0, "multiselect":0, "values":["Source 4"], "replace":0}]' -X POST``

Example Response

``Status: 200 OK``

Parameters

The API expects an array of objects requiring the following parameters.

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| field                 | string                | The unique            |
|                       |                       | field/metadata code   |
|                       |                       | to update. CAPTION    |
|                       |                       | and KEYWORD cannot be |
|                       |                       | modified.             |
+-----------------------+-----------------------+-----------------------+
| multiselect           | integer               | Either 1              |
|                       |                       | (multiselect) or 0    |
|                       |                       | (select).             |
+-----------------------+-----------------------+-----------------------+
| sort                  | integer               | Either 1 for the      |
|                       |                       | values to be sorted   |
|                       |                       | on insertion or 0 as  |
|                       |                       | is. Default is 0      |
|                       |                       | since this is         |
|                       |                       | optional.             |
+-----------------------+-----------------------+-----------------------+
| values                | array                 | Array of values for   |
|                       |                       | the metadata.         |
+-----------------------+-----------------------+-----------------------+
| replace               | integer               | Integer for the type  |
|                       |                       | of action. Either 0   |
|                       |                       | (add new values. No   |
|                       |                       | duplicates accepted), |
|                       |                       | 1 (replace all values |
|                       |                       | with the new values), |
|                       |                       | or 2 (remove values.  |
|                       |                       | Throws an error if    |
|                       |                       | the value does not    |
|                       |                       | exist), or 3 (replace |
|                       |                       | existing values by    |
|                       |                       | associated key with   |
|                       |                       | new values. Requires  |
|                       |                       | format: values:       |
|                       |                       | {"Search for          |
|                       |                       | value":"Replace with  |
|                       |                       | value"} and replaces  |
|                       |                       | in the order that     |
|                       |                       | they are received))   |
+-----------------------+-----------------------+-----------------------+

.. _lightboxes-1:

Lightboxes
----------

.. _lightboxjson:

Lightbox JSON Format
~~~~~~~~~~~~~~~~~~~~

+------------------+-----------+-----------------------------------------------+
| Attribute        | Type      | Description                                   |
+==================+===========+===============================================+
| type             | string    | This is equal to "lightbox".                  |
+------------------+-----------+-----------------------------------------------+
| id               | long      | The unique id of the lightbox.                |
+------------------+-----------+-----------------------------------------------+
| name             | string    | The name of the lightbox.                     |
+------------------+-----------+-----------------------------------------------+
| description      | string    | The description of the lightbox.              |
+------------------+-----------+-----------------------------------------------+
| project          | string    | The project name of the lightbox.             |
+------------------+-----------+-----------------------------------------------+
| datecreated      | string    | The date the lightbox was created.            |
+------------------+-----------+-----------------------------------------------+
| user             | Mini user | The mini user JSON of the owner of the asset. |
+------------------+-----------+-----------------------------------------------+
| share            | boolean   | This lightbox was shared by another user.     |
+------------------+-----------+-----------------------------------------------+
| canedit          | boolean   | Current user can edit lightbox.               |
+------------------+-----------+-----------------------------------------------+
| numCollaborators | integer   | The number of collaborators of this lightbox. |
+------------------+-----------+-----------------------------------------------+
| numComments      | integer   | The number of comments on this lightbox.      |
+------------------+-----------+-----------------------------------------------+
| numberitems      | integer   | How many assets are in the lightbox.          |
+------------------+-----------+-----------------------------------------------+

.. _getlightboxes:

Get current users lightboxes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``GET /lightboxes``

Curl

``curl https://apiv2.webdamdb.com/lightboxes``

Example Response

``Status: 200 OK``

.. code:: json

  [
      {
          "type": "lightbox",
          "id": "12724",
          "name": "Copy o Ne2123",
          "description": "This is really cool",
          "project": "My Project",
          "numItems": "61",
          "share": "false",
          "canedit": "true",
          "numCollaborators": "0",
          "numComments": "0",
        "user": {
          "type": "user",
          "id": "9750",
          "email": "jsmith@example.com",
          "name": "John Smith",
          "username": "myusername"
        }
      },
      {
          "type": "lightbox",
          "id": "12782",
          "name": "Designs",
          "description": "Used for WIP.",
          "project": "Project X",
          "numItems": "5",
          "share": "true",
          "canedit": "true",
          "numCollaborators": "3",
          "numComments": "2",
        "user": {
          "type": "user",
          "id": "9750",
          "email": "jsmith@example.com",
          "name": "John Smith",
          "username": "myusername"
        }
      }
  ]

.. _getlightbox:

Get lightbox information
~~~~~~~~~~~~~~~~~~~~~~~~

``GET /lightboxes/:lightboxid``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/12323``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "type": "lightbox",
    "id": "12782",
    "name": "Designs",
    "description": "Used for WIP.",
    "project": "Project X",
    "numItems": "5",
    "share": "true",
    "canedit": "true",
    "numCollaborators": "3",
    "numComments": "0",
      "user": {
      "type": "user",
      "id": "9750",
      "email": "jsmith@example.com",
      "name": "John Smith",
      "username": "myusername"
    }
  }

.. _createlightbox:

Create a lightbox
~~~~~~~~~~~~~~~~~

``POST /lightboxes``

Curl

``curl https://apiv2.webdamdb.com/lightboxes -d '{"name":"Working on assets","project":"Project X","description":"Used to source assets"}' -X POST``

Example Response

``Status: 201 Created``

.. code:: json

  {
    "type": "lightbox",
    "id": "127822",
    "name": "Working on assets",
    "description": "Used to source assets",
    "project": "Project X",
    "numItems": "5",
    "share": "true",
    "canedit": "true",
    "numCollaborators": "3",
    "numComments": "0",
    "user": {
      "type": "user",
      "id": "9750",
      "email": "jsmith@example.com",
      "name": "John Smith",
      "username": "myusername"
    }
  }

.. _editlightbox:

Edit a lightbox
~~~~~~~~~~~~~~~

``PUT /lightboxes/:lightboxid``

Curl

``curl https://apiv2.webdamdb.com/lightboxes -d '{"id":1123,"name":"Assets to source for campaign"}' -X PUT``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "type": "lightbox",
    "id": "12782",
    "name": "Assets to source for campaign",
    "description": "Used for WIP.",
    "project": "Project X",
    "numItems": "5",
    "share": "true",
    "canedit": "true",
    "numCollaborators": "3",
    "numComments": "0",
      "user": {
      "type": "user",
      "id": "9750",
      "email": "jsmith@example.com",
      "name": "John Smith",
      "username": "myusername"
    }
  }

.. _deletelightbox:

Delete a lightbox
~~~~~~~~~~~~~~~~~

``DELETE /lightboxes/:lightboxid``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/808232 -X DELETE``

Example Response

``Status: 204 OK``

.. _getlightboxassets:

List assets for a lightbox
~~~~~~~~~~~~~~~~~~~~~~~~~~

``GET /lightboxes/:lightboxid/assets``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/808232/assets?sortby=filename&sortdir=desc&limit=20&offset=0``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| sortby                | string                | The field to sort by. |
|                       |                       | Possible values are   |
|                       |                       | filename, filesize,   |
|                       |                       | datecreated and       |
|                       |                       | datemodified.         |
|                       |                       | (Default=datecreated) |
+-----------------------+-----------------------+-----------------------+
| sortdir               | string                | The direction to sort |
|                       |                       | by. Possible values   |
|                       |                       | are asc or desc.      |
|                       |                       | (Default=asc)         |
+-----------------------+-----------------------+-----------------------+
| limit                 | integer               | The number of items   |
|                       |                       | to return.            |
|                       |                       | (Default=50,          |
|                       |                       | Maximum=100)          |
+-----------------------+-----------------------+-----------------------+
| offset                | integer               | The item number to    |
|                       |                       | start with. Default   |
|                       |                       | is 0.                 |
+-----------------------+-----------------------+-----------------------+
| types                 | string                | The file type filters |
|                       |                       | (Available filters:   |
|                       |                       | image, audiovideo,    |
|                       |                       | document,             |
|                       |                       | presentation, other)  |
+-----------------------+-----------------------+-----------------------+
| thumbnail_ttl         | string                | Time to live for      |
|                       |                       | thumbnails            |
|                       |                       | Default: Set by the   |
|                       |                       | account admin         |
|                       |                       | Values: '+3 min',     |
|                       |                       | '+15 min', '+2        |
|                       |                       | hours', '+1 day', '+2 |
|                       |                       | weeks',               |
|                       |                       | 'no-expiration'       |
+-----------------------+-----------------------+-----------------------+

Example Response

``Status: 200 OK``

.. code:: json

  {
    "total_count": "1",
    "offset": 0,
    "limit": "50",
    "facets": {
      "types": {
        "image": "6",
        "document": "1",
        "audiovideo": "1",
        "presentation": "3",
        "other": null
      }
    },
    "items": [
      {
        "type": "asset",
        "id": "3456621",
        "status": "active",
        "filename": "Lightbox_switch.jpg",
        "name": "Lightbox_switch.jpg",
        "filesize": "0.17",
        "width": "890",
        "height": "748",
        "description": "",
        "filetype": "jpg",
        "colorspace": "RGB",
        "version": "1",
        "datecreated": "2013-07-10 14:30:25",
        "datemodified": "2013-07-10 14:30:25",
        "thumbnailurls": [
          { "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_9wFXFzBwv6.jpg" },
          { "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_9wFXFzBwv6.jpg" },
          { "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_9wFXFzBwv6.jpg" },
          { "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_9wFXFzBwv6.jpg" },
          { "size": "550", "url": "http://subdomain.webdamdb.com/image_dir/album90922/md_9wFXFzBwv6.jpg" }
        ],
        "folder": {
          "type": "folder",
          "id": "90922",
          "name": "WORKS22"
        },
        "numComments":2,
        "user": {
          "type": "user",
          "id": "9750",
          "email": "jsmith@example.com",
          "name": "John Smith",
          "username": "myusername"
        }
      }
    ]
  }

.. _addlightboxasset:

Add asset to a lightbox
~~~~~~~~~~~~~~~~~~~~~~~

``POST /lightboxes/:lightboxid/assets``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/34543543/assets -d '{"id":"2342211"}' -X POST``

Example Response

``Status: 201 Created``

.. code:: json

  {
      "type": "asset",
      "id": "2342211",
  }

.. _removelightboxasset:

Remove asset from a folder
~~~~~~~~~~~~~~~~~~~~~~~~~~

``DELETE /lightboxes/:lightboxid/assets/:assetid``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/1223423/assets/123333 -X DELETE``

Example Response

``Status: 204 OK``

.. _emptylightbox:

Empty a lightbox
~~~~~~~~~~~~~~~~

``DELETE /lightboxes/:lightboxid/empty``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/1223423/empty -X DELETE``

Example Response

``Status: 204 OK``

.. _getlightboxcollaborators:

List collaborators for a lightbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``GET /lightboxes/:lightboxid/collaborators``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/23423422/collaborators``

Example Response

``Status: 200 OK``

.. code:: json

  [
      {
          "type": "collaborator",
          "id": "12814",
          "email": "sjan@example.com",
          "canedit": "true"
      },
      {
          "type": "collaborator",
          "id": "12816",
          "email": "jsmith@example.com",
          "user": {
              "type": "user",
              "id": "9810",
              "email": "jsmith@example.com",
              "name": "John Smith",
              "username": "jsmith"
          },
          "canedit": "true"
      }
  ]

.. _addlightboxcollaborator:

Add collaborator to a lightbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``POST /lightboxes/:lightboxid/collaborators``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/:lightboxid/collaborators -d '{"emails":["collab@example.com","collab2@example.com"],"message":"This lightbox has cool assets.","canedit":true}' -X POST``

Example Response

``Status: 201 Created``

.. code:: json

  {
      "type": "collaborator",
      "id": "12814",
      "emails": ["colab@example.com"],
      "canedit": "true"
  }

.. _removelightboxcollaborator:

Remove a collaborator from a lightbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``DELETE /lightboxes/:lightboxid/collaborators/:collaboratorid``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/12132/collaborators/13422 -X DELETE``

Example Response

``Status: 204 OK``

.. _sendlightboxdownload:

Send lightbox download
~~~~~~~~~~~~~~~~~~~~~~

``POST /lightboxes/:lightboxid/senddownload``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/7812323/senddownload -d '{"emails":["userone@emaildomain.com", "usertwo@emaildomain.com"], "subject": "Cool lightbox", "message": "Hi, this lightbox has very cool assets", "expirationdate": "2013-12-07"}' -X POST``

Example Response

``Status: 200 OK``

.. code:: json

  {
      "downloadkey": "qOF1NRU40myI7S3f"
  }

Lightbox Comments
-----------------

.. _getlightboxcomments:

List comments on a lightbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``GET /lightboxes/:lightboxid/comments``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/23423422/comments``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "total_items":"1",
    "items":[
        {
          "type":"comment",
          "id":"643",
          "comment":"This is the best asset.",
          "datecreated":"2013-10-15 21:53:24",
          "datemodified":"2013-10-15 21:53:24",
          "item":{
              "type":"lightbox",
              "id":"12782"
          },
          "user":{
              "type":"user",
              "id":"123123",
              "email":"james@gmail.com",
              "name":"John Doe",
              "username":"myusername"
          }
        }
    ]
  }

.. _getlightboxcomment:

Get a lightbox comment
~~~~~~~~~~~~~~~~~~~~~~

``GET /lightboxes/:lightboxid/comments/:commentid``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/23423422/comments/1233``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "type":"comment",
    "id":"643",
    "comment":"This is the best asset.",
    "datecreated":"2013-10-15 21:53:24",
    "datemodified":"2013-10-15 21:53:24",
    "item":{
      "type":"lightbox",
      "id":"12782"
    },
    "user":{
      "type":"user",
      "id":"123123",
      "email":"james@gmail.com",
      "name":"John Doe",
      "username":"myusername"
    }
  }

.. _addlightboxcomment:

Add comment to a lightbox
~~~~~~~~~~~~~~~~~~~~~~~~~

``POST /lightboxes/:lightboxid/comments``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/:lightboxid/comments -d '{"type":"comment","comment":"This asset is the best."}' -X POST``

Example Response

``Status: 201 Created``

.. code:: json

  {
    "type":"comment",
    "id":"643",
    "comment":"This is the best asset.",
    "datecreated":"2013-10-15 21:53:24",
    "datemodified":"2013-10-15 21:53:24",
    "item":{
      "type":"lightbox",
      "id":"12782"
    },
    "user":{
      "type":"user",
      "id":"123123",
      "email":"james@gmail.com",
      "name":"John Doe",
      "username":"myusername"
    }
  }

.. _deletelightboxcomment:

Delete a comment from a lightbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``DELETE /lightboxes/:lightboxid/comments/:commentid``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/12132/comments/13422 -X DELETE``

Example Response

``Status: 204 OK``

.. _getlightboxassetcomments:

List comments on an asset in lightbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``GET /lightboxes/:lightboxid/assets/:assetid/comments``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/23423422/assets/4322322/comments``

Example Response

``Status: 200 OK``

.. code:: json

  {
    "total_items":"1",
    "items":[
        {
          "type":"comment",
          "id":"643",
          "comment":"This is the best asset.",
          "datecreated":"2013-10-15 21:53:24",
          "datemodified":"2013-10-15 21:53:24",
          "item":{
              "type":"lightbox",
              "id":"12782"
          },
          "user":{
              "type":"user",
              "id":"123123",
              "email":"james@gmail.com",
              "name":"John Doe",
              "username":"myusername"
          }
        }
    ]
  }
.. _getlightboxassetcomment:

Get comment on an asset in lightbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``GET /lightboxes/:lightboxid/assets/:assetid/comments/:commentid``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/23423422/assets/54342/comments/1233``

Example Response

``Status: 200 OK``

.. code:: json

  {
      "type":"comment",
      "id":"643",
      "comment":"This is the best asset.",
      "datecreated":"2013-10-15 21:53:24",
      "datemodified":"2013-10-15 21:53:24",
      "item":{
        "type":"lightbox",
        "id":"12782"
      },
      "user":{
        "type":"user",
        "id":"123123",
        "email":"james@gmail.com",
        "name":"John Doe",
        "username":"myusername"
      }
  }

.. _addlightboxassetcomment:

Add comment to an asset in lightbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``POST /lightboxes/:lightboxid/assets/:assetid/comments``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/:lightboxid/assets/:assetid/comments -d '{"type":"comment","comment":"This asset is the best."}' -X POST``

Example Response

``Status: 201 Created``

.. code:: json

  {
      "type":"comment",
      "id":"643",
      "comment":"This is the best asset.",
      "datecreated":"2013-10-15 21:53:24",
      "datemodified":"2013-10-15 21:53:24",
      "item":{
        "type":"lightbox",
        "id":"12782"
      },
      "user":{
        "type":"user",
        "id":"123123",
        "email":"james@gmail.com",
        "name":"John Doe",
        "username":"myusername"
      }
  }

.. _deletelightboxassetcomment:

Delete a comment on an asset in lightbox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``DELETE /lightboxes/:lightboxid/assets/:assetid/comments/:commentid``

Curl

``curl https://apiv2.webdamdb.com/lightboxes/12132/assets/424234/comments/13422 -X DELETE``

Example Response

``Status: 204 OK``

Search
------

.. _searchassets:

Search assets
~~~~~~~~~~~~~

.. note:: You may only search one Search Field at a time using the Search API.

Only the parameters listed in this section are supported.

``GET /search``

Curl

``curl https://apiv2.webdamdb.com/search?sortby=filename&sortdir=desc&limit=20&offset=0&query=dog&folderid=405352``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| query                 | string                | The text to perform   |
|                       |                       | the search. This      |
|                       |                       | field is required.    |
+-----------------------+-----------------------+-----------------------+
| folderid              | integer               | The folder id to      |
|                       |                       | filter search results |
|                       |                       | by specific           |
|                       |                       | |acquia-product:dam|  |
|                       |                       | folder.               |
+-----------------------+-----------------------+-----------------------+
| sortby                | string                | The field to sort by. |
|                       |                       | Possible values are   |
|                       |                       | filename, filesize,   |
|                       |                       | datecreated and       |
|                       |                       | datemodified.         |
|                       |                       | (Default=datecreated) |
+-----------------------+-----------------------+-----------------------+
| sortdir               | string                | The direction to sort |
|                       |                       | by. Possible values   |
|                       |                       | are asc or desc.      |
|                       |                       | (Default=asc)         |
+-----------------------+-----------------------+-----------------------+
| limit                 | integer               | The number of items   |
|                       |                       | to return.            |
|                       |                       | (Default=50,          |
|                       |                       | Maximum=100)          |
+-----------------------+-----------------------+-----------------------+
| offset                | integer               | The item number to    |
|                       |                       | start with. Default   |
|                       |                       | is 0.                 |
+-----------------------+-----------------------+-----------------------+
| types                 | string                | The file type filters |
|                       |                       | (Available filters:   |
|                       |                       | image, audiovideo,    |
|                       |                       | document,             |
|                       |                       | presentation, other)  |
+-----------------------+-----------------------+-----------------------+
| searchfield           | string                | The metadatafield     |
|                       |                       | filters (Available    |
|                       |                       | filters:              |
|                       |                       | customfield1,         |
|                       |                       | language, headline,   |
|                       |                       | keyword, other)       |
+-----------------------+-----------------------+-----------------------+
| Time to live for      |                       |                       |
| thumbnails            |                       |                       |
| Default: Set by the   |                       |                       |
| account admin         |                       |                       |
| Values: '+3 min',     |                       |                       |
| '+15 min', '+2        |                       |                       |
| hours', '+1 day', '+2 |                       |                       |
| weeks',               |                       |                       |
| 'no-expiration'       |                       |                       |
+-----------------------+-----------------------+-----------------------+

Example Response

``Status: 200 OK``

.. code:: json

  {
    "total_count": "1",
    "offset": 0,
    "limit": "50",
    "facets": {
      "types": {
        "image": "6",
        "document": "1",
        "audiovideo": "1",
        "presentation": "3",
        "other": null
      }
    },
    "items": [
      {
        "type": "asset",
        "id": "3456621",
        "status": "active",
        "filename": "Lightbox_switch.jpg",
        "name": "Lightbox_switch.jpg",
        "filesize": "0.17",
        "width": "890",
        "height": "748",
        "description": "",
        "filetype": "jpg",
        "colorspace": "RGB",
        "version": "1",
        "datecreated": "2013-07-10 14:30:25",
        "datemodified": "2013-07-10 14:30:25",
        "thumbnailurls": {
          { "size": "100", "url": "http://subdomain.webdamdb.com/s/100th_sm_9wFXFzBwv6.jpg" },
          { "size": "150", "url": "http://subdomain.webdamdb.com/s/150th_sm_9wFXFzBwv6.jpg" },
          { "size": "220", "url": "http://subdomain.webdamdb.com/s/220th_sm_9wFXFzBwv6.jpg" },
          { "size": "310", "url": "http://subdomain.webdamdb.com/s/310th_sm_9wFXFzBwv6.jpg" },
          { "size": "550", "url": "http://subdomain.webdamdb.com/s/550th_sm_9wFXFzBwv6.jpg" }
        },
        "folder": {
          "type": "folder",
          "id": "90922",
          "name": "WORKS22"
        },
        "user": {
          "type": "user",
          "id": "9750",
          "email": "jsmith@example.com",
          "name": "John Smith",
          "username": "myusername"
        }
      }
    ]
  }

.. _groups-1:

Groups
------

.. _groupjson:

Group JSON Format
~~~~~~~~~~~~~~~~~

+-------------+---------+-----------------------------------+
| Attribute   | Type    | Description                       |
+=============+=========+===================================+
| type        | string  | This is equal to "group".         |
+-------------+---------+-----------------------------------+
| id          | long    | The unique id of the group.       |
+-------------+---------+-----------------------------------+
| role        | string  | The role of the group.            |
+-------------+---------+-----------------------------------+
| name        | string  | The name of the group.            |
+-------------+---------+-----------------------------------+
| description | string  | The description of the group.     |
+-------------+---------+-----------------------------------+
| numusers    | integer | How many users are in the folder. |
+-------------+---------+-----------------------------------+

.. _getgroups:

Get all groups
~~~~~~~~~~~~~~

``GET /groups``

| *Allowed For*
| Admins

Curl

``curl https://apiv2.webdamdb.com/groups``

Example Response

``Status: 200 OK``

.. code:: json

  [
    {
      "type": "group",
      "id": "162",
      "name": "Marketing Asia",
      "description": "This group is for marketing in Asia",
      "role": "Contributor",
      "numusers": 2
    },
      {
      "type": "group",
      "id": "165",
      "name": "Partners",
      "description": "This group is for our partners",
      "role": "End User",
      "numusers": 6
    }
  ]

.. _getgroup:

Get group information
~~~~~~~~~~~~~~~~~~~~~

``GET /groups/:groupid``

| *Allowed For*
| Admins

Curl

``curl https://apiv2.webdamdb.com/groups/162``

Example Response

``Status: 200 OK``

.. code:: json

  {
      "type": "group",
      "id": "162",
      "name": "Marketing Asia",
      "description": "This group is for marketing in Asia",
      "role": "Contributor",
      "numusers": 2
  }

.. _creategroup:

Create a group
~~~~~~~~~~~~~~

``POST /groups``

| *Allowed For*
| Admins

Curl

``curl https://apiv2.webdamdb.com/groups -d '{"type":"group","id":"162","name":"Marketing Asia","description":"dont tread on me","role":"Contributor"}' -X POST``

Example Response

``Status: 201 Created``

.. code:: json

  {
      "type": "group",
      "id": "162",
      "name": "Marketing Asia",
      "description": "This group is for marketing in Asia",
      "role": "Contributor",
      "numusers": 0
  }

.. _editgroup:

Edit a group
~~~~~~~~~~~~

``PUT /groups/:groupid``

| *Allowed For*
| Admins

Curl

``curl https://apiv2.webdamdb.com/groups/162 -d '{"id":"162","name":"Marketing South Asia"}' -X PUT``

Example Response

``Status: 200 OK``

.. code:: json

  {
      "type": "group",
      "id": "162",
      "name": "Marketing South Asia",
      "description": "This group is for marketing in Asia",
      "role": "Contributor",
      "numusers": 0
  }

.. _deletegroup:

Delete a group
~~~~~~~~~~~~~~

``DELETE /groups/:groupid``

| *Allowed For*
| Admins

Curl

``curl https://apiv2.webdamdb.com/groups/162 -X DELETE``

Example Response

``Status: 204 OK``

.. _getgroupusers:

View users of a group
~~~~~~~~~~~~~~~~~~~~~

``GET /groups/:groupid/users``

| *Allowed For*
| Admins

Curl

``curl https://apiv2.webdamdb.com/groups/23422/users``

Example Response

``Status: 200 OK``

.. code:: json

  [
    {
    "user": {
      "type": "user",
      "id": "9750",
      "email": "colab@example.com",
      "name": "Celeb Stars",
      "username": "myusername"
      }
    },
      {
      "user": {
      "type": "user",
      "id": "9754",
      "email": "jsmith@example.com",
      "name": "John Smith",
      "username": "jsmith"
     }
    }
  ]

.. _addusertogroup:

Add user to a group
~~~~~~~~~~~~~~~~~~~

``POST /groups/:groupid/users/:userid``

| *Allowed For*
| Admins

Curl

``curl https://apiv2.webdamdb.com/groups/23422/users/923422 -X POST``

Example Response

``Status: 201 Created``

.. code:: json

  {
    "user": {
    "type": "user",
    "id": "9750",
    "email": "colab@example.com",
    "name": "Celeb Stars",
    "username": "myusername"
    }
}

.. _removeuserfromgroup:

Remove user from group
~~~~~~~~~~~~~~~~~~~~~~

``POST /groups/:groupid/users/:userid``

| *Allowed For*
| Admins

Curl

``curl https://apiv2.webdamdb.com/groups/23422/users/923422 -X DELETE``

Example Response

``Status: 204 OK``

.. _users-1:

Users
-----

.. _userjson:

User JSON Format
~~~~~~~~~~~~~~~~

+-----------------------+-----------------------+-----------------------+
| Attribute             | Type                  | Description           |
+=======================+=======================+=======================+
| type                  | string                | This is equal to      |
|                       |                       | "user"                |
+-----------------------+-----------------------+-----------------------+
| id                    | long                  | The unique id of the  |
|                       |                       | user.                 |
+-----------------------+-----------------------+-----------------------+
| username              | string                | The username for the  |
|                       |                       | user.                 |
+-----------------------+-----------------------+-----------------------+
| first                 | string                | The first name of the |
|                       |                       | user.                 |
+-----------------------+-----------------------+-----------------------+
| last                  | string                | The first last of the |
|                       |                       | user.                 |
+-----------------------+-----------------------+-----------------------+
| name                  | string                | The fullname of the   |
|                       |                       | user.                 |
+-----------------------+-----------------------+-----------------------+
| email                 | string                | The email address of  |
|                       |                       | the user.             |
+-----------------------+-----------------------+-----------------------+
| company               | date                  | The company name the  |
|                       |                       | user works for.       |
+-----------------------+-----------------------+-----------------------+
| companyurl            | string                | The company url the   |
|                       |                       | user works for.       |
+-----------------------+-----------------------+-----------------------+
| phone                 | string                | Phone number of user. |
+-----------------------+-----------------------+-----------------------+
| fax                   | string                | Fax number of user.   |
+-----------------------+-----------------------+-----------------------+
| country               | string                | The country the user  |
|                       |                       | is in.                |
+-----------------------+-----------------------+-----------------------+
| city                  | string                | The city the user is  |
|                       |                       | in.                   |
+-----------------------+-----------------------+-----------------------+
| address1              | string                | The street address    |
|                       |                       | the user works.       |
+-----------------------+-----------------------+-----------------------+
| address2              | string                | The street secondary  |
|                       |                       | address the user      |
|                       |                       | works.                |
+-----------------------+-----------------------+-----------------------+
| status                | string                | The current state of  |
|                       |                       | the user, either      |
|                       |                       | active or inactive.   |
+-----------------------+-----------------------+-----------------------+
| datecreated           | date                  | The date the user was |
|                       |                       | created.              |
+-----------------------+-----------------------+-----------------------+
| lastlogin             | date                  | The timestamp of      |
|                       |                       | users last sign-in.   |
+-----------------------+-----------------------+-----------------------+
| sendemail             | boolean               | Send welcome email    |
|                       |                       | when user account is  |
|                       |                       | created.              |
+-----------------------+-----------------------+-----------------------+
| groups                | array                 | Array of group        |
|                       |                       | objects that the user |
|                       |                       | belongs to.           |
+-----------------------+-----------------------+-----------------------+

.. _getusers:

Get users
~~~~~~~~~

``GET /users``

| *Allowed For*
| Admins

Curl

``curl https://apiv2.webdamdb.com/users?offset=0&limit=1&sortby=username&sortdir=asc``

Parameters

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+=======================+=======================+=======================+
| sortby                | string                | The field to sort by. |
|                       |                       | Possible values are   |
|                       |                       | username, firstname,  |
|                       |                       | lastname and email.   |
|                       |                       | (Default=username)    |
+-----------------------+-----------------------+-----------------------+
| sortdir               | string                | The direction to sort |
|                       |                       | by. Possible values   |
|                       |                       | are asc or desc.      |
|                       |                       | (Default=asc)         |
+-----------------------+-----------------------+-----------------------+
| limit                 | integer               | The number of items   |
|                       |                       | to return.            |
|                       |                       | (Default=1000,        |
|                       |                       | Maximum=1000)         |
+-----------------------+-----------------------+-----------------------+
| offset                | integer               | The item number to    |
|                       |                       | start with. Default   |
|                       |                       | is 0.                 |
+-----------------------+-----------------------+-----------------------+

Example Response

``Status: 200 OK``

.. code:: json

  [
    {
      "type": "user",
      "id": "9769",
      "username": "jsmith",
      "first": "John",
      "last": "Smith",
      "name": "John Smith",
      "email": "contrib@example.com",
      "datecreated": "2009-10-09 20:34:36",
      "lastlogin": "2013-07-10 12:04:24",
      "company": "",
      "companyurl": "",
      "phone": "",
      "fax": "",
      "country": "United States",
      "city": "",
      "address1": "",
      "address2": "",
      "zip": "94402",
      "groups": [
          {
              "type": "group",
              "id": "21",
              "name": "Admin",
              "role": "Admin"
          }
      ]
    }
  ]

.. _getcurrentuser:

Get current user
~~~~~~~~~~~~~~~~

``GET /users/me``

Curl

``curl https://apiv2.webdamdb.com/users/me``

Example Response

``Status: 200 OK``

.. code:: json

  {
      "type": "user",
      "id": "9769",
      "username": "jsmith",
      "first": "John",
      "last": "Smith",
      "name": "John Smith",
      "email": "contrib@example.com",
      "datecreated": "2009-10-09 20:34:36",
      "lastlogin": "2013-07-10 12:04:24",
      "company": "",
      "companyurl": "",
      "phone": "",
      "fax": "",
      "country": "United States",
      "city": "",
      "address1": "",
      "address2": "",
      "zip": "94402",
      "groups": [
          {
              "type": "group",
              "id": "21",
              "name": "Admin",
              "role": "Admin"
          }
      ]
  }

.. _getuser:

Get a user
~~~~~~~~~~

``GET /users/9769``

| *Allowed For*
| Admins

Curl

``curl https://apiv2.webdamdb.com/users/9769``

Example Response

``Status: 200 OK``

.. code:: json

  {
      "type": "user",
      "id": "9769",
      "username": "jsmith",
      "first": "John",
      "last": "Smith",
      "name": "John Smith",
      "email": "contrib@example.com",
      "datecreated": "2009-10-09 20:34:36",
      "lastlogin": "2013-07-10 12:04:24",
      "company": "",
      "companyurl": "",
      "phone": "",
      "fax": "",
      "country": "United States",
      "city": "",
      "address1": "",
      "address2": "",
      "zip": "94402"
  }

.. _getusergroups:

View groups for a user
~~~~~~~~~~~~~~~~~~~~~~

``GET /users/9769/groups``

| *Allowed For*
| Admins

Curl

``curl https://apiv2.webdamdb.com/users/9769/groups``

Example Response

``Status: 200 OK``

.. code:: json

  [
    {
        "type": "group",
        "id": "154",
        "name": "Sales",
        "role": "End user"
    },
    {
        "type": "group",
        "id": "138",
        "name": "Marketing",
        "role": "Contributor"
    }
  ]
.. _createuser:

Create a user
~~~~~~~~~~~~~

``POST /users``

| *Allowed For*
| Admins

Curl

``curl https://apiv2.webdamdb.com/users -d '{"username":"90784","password1":"password@12","password2":"password@12","first":"John","last":"smith","email":contrib@example.com","country": "United States","zip": "94402,"sendemail": "true","status":"active"}' -X POST``

Example Response

``Status: 201 Created``

.. code:: json

  {
      "type": "user",
      "id": "9769",
      "username": "jsmith",
      "password1":"password@12",
      "password2":"password@12",
      "first": "John",
      "last": "Smith",
      "name": "John Smith",
      "email": "contrib@example.com",
      "datecreated": "2013-07-10 12:04:24",
      "lastlogin": "2013-07-10 12:04:24",
      "company": "",
      "companyurl": "",
      "phone": "",
      "fax": "",
      "country": "United States",
      "city": "",
      "address1": "",
      "address2": "",
      "zip": "94402",
      "status": "active",
      "sendemail": "true"
  }

.. _edituser:

Edit a user
~~~~~~~~~~~

``PUT /users/:userid`` or ``PUT /users/me``

Curl

``curl https://apiv2.webdamdb.com/users/me -d '{"id":12321","email":"contrib2@example.com","zip":"94065"}' -X PUT``

Example Response

``Status: 200 OK``

.. code:: json

  {
      "type": "user",
      "id": "9769",
      "username": "jsmith",
      "first": "John",
      "last": "Smith",
      "name": "John Smith",
      "email": "contrib2@example.com",
      "datecreated": "2013-07-10 12:04:24",
      "lastlogin": "2013-07-10 12:04:24",
      "company": "",
      "companyurl": "",
      "phone": "",
      "fax": "",
      "country": "United States",
      "city": "",
      "address1": "",
      "address2": "",
      "zip": "94065"
  }

.. _deleteuser:

Delete a user
~~~~~~~~~~~~~

``DELETE /users/:userid``

*Allowed For* - Admins

Curl

``curl https://apiv2.webdamdb.com/users/9769 -X DELETE``

Example Response

``Status: 204 OK``

.. _account-1:

Account
-------

.. _accountsubscription:

Get account subscription
~~~~~~~~~~~~~~~~~~~~~~~~

``GET /subscription``

Curl

``curl https://apiv2.webdamdb.com/subscription``

Example Response

``Status: 200 OK``

.. code:: json

  {
      "maxEndUsers": "125",
      "numEndUsers": 50,
      "maxPowerUsers": "125",
      "numPowerUsers": 48,
      "maxUsers": "125",
      "url": "account.webdamdb.com",
      "username": "username",
      "planDiskSpace": "10000 MB",
      "currentDiskSpace": "361 MB",
      "activeUsers": "30",
      "inactiveUsers": "8"
  }

.. _notifications-1:

Notifications
-------------

.. _availablenotificationtypes:

Available actions
~~~~~~~~~~~~~~~~~

+-----------------------+---------------------------------------------------+
| Action                | Description                                       |
+=======================+===================================================+
| asset_created         | A user uploaded asset(s) to a folder              |
+-----------------------+---------------------------------------------------+
| asset_deleted         | A user deleted asset(s) from a folder             |
+-----------------------+---------------------------------------------------+
| asset_version         | A user uploaded a new asset version               |
+-----------------------+---------------------------------------------------+
| asset_property        | A user edited metadata of asset(s)                |
+-----------------------+---------------------------------------------------+
| asset_add_lightbox    | A user added asset(s) to a lightbox               |
+-----------------------+---------------------------------------------------+
| asset_remove_lightbox | A user removed asset(s) from a lightbox           |
+-----------------------+---------------------------------------------------+
| lightbox_share        | A user shared a lightbox with you                 |
+-----------------------+---------------------------------------------------+
| lightbox_sharedelete  | A user removed a shared lightbox                  |
+-----------------------+---------------------------------------------------+
| comment               | A user commented on a lightbox                    |
+-----------------------+---------------------------------------------------+
| message               | Site admin sent a message                         |
+-----------------------+---------------------------------------------------+
| user_registered       | A new user registered                             |
+-----------------------+---------------------------------------------------+
| download_request      | A user/visitor is requesting to download an asset |
+-----------------------+---------------------------------------------------+

Get notifications

``GET /notifications?limit=20&offset=0``

Curl

``curl https://apiv2.webdamdb.com/notifications?limit=20&offset=0``

Example Response

``Status: 200 OK``

.. code:: json

  {  
    "last_read":"2013-11-14 18:23:13",
    "offset":"0",
    "limit":"20",
    "total":"65",
    "notifications":[  
      {  
        "id":"2952",
        "type":"notification",
        "action":"comment",
        "datecreated":"2013-11-13 20:55:38",
        "user":{  
          "type":"user",
          "id":"31885",
          "email":"user@emaildomain.com",
          "name":"Kim Jane",
          "username":"kjane",
          "status":"active"
        },
        "source":{  
          "type":"lightbox",
          "id":"39438",
          "name":"Summer publication"
        },
        "subitems":{  
          "type":"comment",
          "comment":"I like these images"
        },
        "displaystring":"Kim Jane commented on Summer publication, 'I like these images'"
      },
      {  
        "id":"2951",
        "type":"notification",
        "action":"asset_version",
        "datecreated":"2013-11-13 10:32:51",
        "user":{  
          "type":"user",
          "id":"31877",
          "email":"user@emaildomain.com",
          "name":"Abbey Johnson",
          "username":"ajohn",
          "status":"active"
        },
        "source":{  
          "type":"asset",
          "id":"5994050",
          "name":"sales101.ppt",
          "version":"3"
        },
        "displaystring":"Abbey Johnson updated sales101.ppt to version 3"
      },
      {  
        "id":"2950",
        "type":"notification",
        "action":"asset_deleted",
        "datecreated":"2013-11-13 09:17:50",
        "user":{  
          "type":"user",
          "id":"31877",
          "email":"user@emaildomain.com",
          "name":"Abbey Johnson",
          "username":"ajohn",
          "status":"active"
        },
        "subitems":[  
          {  
            "type":"asset",
            "id":"5994051"
          },
          {  
            "type":"asset",
            "id":"5994364"
          }
        ],
        "source":{  
          "type":"folder",
          "id":"192518",
          "name":"Custom Icons"
        },
        "displaystring":"Abbey Johnson deleted 2 asset(s) from Custom Icons"
      }
    ]
  }

.. _api-reference-1:

API Reference
-------------

EXIF Metadata

+-----------------------------+--------------------------------+
| Field                       | Description                    |
+=============================+================================+
| artist                      | Artist                         |
+-----------------------------+--------------------------------+
| bitspersample               | Bits Per Sample                |
+-----------------------------+--------------------------------+
| colorspace                  | Color Space                    |
+-----------------------------+--------------------------------+
| componentsconfiguration     | Components Configuration       |
+-----------------------------+--------------------------------+
| compressedbitsperpixel      | Compressed Bits Per Pixel      |
+-----------------------------+--------------------------------+
| compression                 | Compression                    |
+-----------------------------+--------------------------------+
| contrast                    | Contrast                       |
+-----------------------------+--------------------------------+
| copyright                   | Copyright                      |
+-----------------------------+--------------------------------+
| customrendered              | Custom Rendered                |
+-----------------------------+--------------------------------+
| datetime                    | Date Time                      |
+-----------------------------+--------------------------------+
| datetimedigitized           | Date Time Digitized            |
+-----------------------------+--------------------------------+
| datetimeoriginal            | Date Time Original             |
+-----------------------------+--------------------------------+
| digitalzoomratio            | Digital Zoom Ratio             |
+-----------------------------+--------------------------------+
| exifimageheight             | Exif Image Length              |
+-----------------------------+--------------------------------+
| exifimagewidth              | Exif Image Width               |
+-----------------------------+--------------------------------+
| exifoffset                  | Exif Offset                    |
+-----------------------------+--------------------------------+
| exifversion                 | Exif Version                   |
+-----------------------------+--------------------------------+
| exposurebiasvalue           | Exposure Bias Value            |
+-----------------------------+--------------------------------+
| exposuremode                | Exposure Mode                  |
+-----------------------------+--------------------------------+
| exposureprogram             | Exposure Program               |
+-----------------------------+--------------------------------+
| exposuretime                | Exposure Time                  |
+-----------------------------+--------------------------------+
| filesource                  | File Source                    |
+-----------------------------+--------------------------------+
| flash                       | Flash                          |
+-----------------------------+--------------------------------+
| flashpixversion             | Flashpix Version               |
+-----------------------------+--------------------------------+
| fnumber                     | F Number                       |
+-----------------------------+--------------------------------+
| focallength                 | Focal Length                   |
+-----------------------------+--------------------------------+
| gaincontrol                 | Gain Control                   |
+-----------------------------+--------------------------------+
| imagedescription            | Image Description              |
+-----------------------------+--------------------------------+
| imagelength                 | Image Length                   |
+-----------------------------+--------------------------------+
| imageniqueid                | Image Unique ID                |
+-----------------------------+--------------------------------+
| imagewidth                  | Image Width                    |
+-----------------------------+--------------------------------+
| interoperabilityindex       | Interoperability Index         |
+-----------------------------+--------------------------------+
| interoperabilityoffset      | Interoperability Offset        |
+-----------------------------+--------------------------------+
| interoperabilityversion     | Interoperability Version       |
+-----------------------------+--------------------------------+
| isospeedratings             | ISO Speed Ratings              |
+-----------------------------+--------------------------------+
| jpeginterchangeformat       | JPEG Interchange Format        |
+-----------------------------+--------------------------------+
| jpeginterchangeformatlength | JPEG Interchange Format Length |
+-----------------------------+--------------------------------+
| lightsource                 | Light Source                   |
+-----------------------------+--------------------------------+
| make                        | Make                           |
+-----------------------------+--------------------------------+
| makernote                   | Maker Note                     |
+-----------------------------+--------------------------------+
| maxaperturevalue            | Max Aperture Value             |
+-----------------------------+--------------------------------+
| meteringmode                | Metering Mode                  |
+-----------------------------+--------------------------------+
| model                       | Model                          |
+-----------------------------+--------------------------------+
| orientation                 | Orientation                    |
+-----------------------------+--------------------------------+
| photometricinterpretation   | Photometric Interpretation     |
+-----------------------------+--------------------------------+
| pixelxdimension             | Pixel X Dimension              |
+-----------------------------+--------------------------------+
| pixelydimension             | Pixel Y Dimension              |
+-----------------------------+--------------------------------+
| planarconfiguration         | Planar Configuration           |
+-----------------------------+--------------------------------+
| primarychromaticities       | Primary Chromaticities         |
+-----------------------------+--------------------------------+
| printimagematching          | Print Image Matching           |
+-----------------------------+--------------------------------+
| referenceblackwhite         | Reference Black White          |
+-----------------------------+--------------------------------+
| relatedsoundfile            | Related SoundFile              |
+-----------------------------+--------------------------------+
| resolutionunit              | Resolution Unit                |
+-----------------------------+--------------------------------+
| rowsperstrip                | Rows Per Strip                 |
+-----------------------------+--------------------------------+
| samplesperpixel             | Samples Per Pixel              |
+-----------------------------+--------------------------------+
| saturation                  | Saturation                     |
+-----------------------------+--------------------------------+
| scenecapturetype            | Scene Capture Type             |
+-----------------------------+--------------------------------+
| sharpness                   | Sharpness                      |
+-----------------------------+--------------------------------+
| software                    | Software                       |
+-----------------------------+--------------------------------+
| stripbytecounts             | Strip Byte Counts              |
+-----------------------------+--------------------------------+
| stripoffsets                | Strip Offsets                  |
+-----------------------------+--------------------------------+
| subsectime                  | Sub Sec Time                   |
+-----------------------------+--------------------------------+
| subsectimedigitized         | Sub Sec Time Digitized         |
+-----------------------------+--------------------------------+
| subsectimeoriginal          | Sub Sec Time Original          |
+-----------------------------+--------------------------------+
| tainted                     | Tainted                        |
+-----------------------------+--------------------------------+
| transferfunction            | Transfer Function              |
+-----------------------------+--------------------------------+
| usercomment                 | User Comment                   |
+-----------------------------+--------------------------------+
| whitebalance                | White Balance                  |
+-----------------------------+--------------------------------+
| whitepoint                  | White Point                    |
+-----------------------------+--------------------------------+
| winxp-author                | WinXP-Author                   |
+-----------------------------+--------------------------------+
| winxp-comments              | WinXP-Comments                 |
+-----------------------------+--------------------------------+
| winxp-keywords              | WinXP-Keywords                 |
+-----------------------------+--------------------------------+
| winxp-subject               | WinXP-Subject                  |
+-----------------------------+--------------------------------+
| winxp-title                 | WinXP-Title                    |
+-----------------------------+--------------------------------+
| xresolution                 | X Resolution                   |
+-----------------------------+--------------------------------+
| ycbcrcoefficients           | YCbCr Coefficients             |
+-----------------------------+--------------------------------+
| ycbcrpositioning            | YCbCr Positioning              |
+-----------------------------+--------------------------------+
| ycbcrsubsampling            | YCbCr SubSampling              |
+-----------------------------+--------------------------------+
| yresolution                 | Y Resolution                   |
+-----------------------------+--------------------------------+

XMP Metadata

+------------------+---------------------------------+
| Field            | Description                     |
+==================+=================================+
| byline           | By-line                         |
+------------------+---------------------------------+
| bytitle          | By-line title                   |
+------------------+---------------------------------+
| caption          | Caption/Abstract                |
+------------------+---------------------------------+
| captionwriter    | Writer/Editor                   |
+------------------+---------------------------------+
| category         | Category                        |
+------------------+---------------------------------+
| city             | City                            |
+------------------+---------------------------------+
| contact          | Contact                         |
+------------------+---------------------------------+
| copyright        | Copyright notice                |
+------------------+---------------------------------+
| countrycode      | Country/Primary location        |
+------------------+---------------------------------+
| countryname      | Country name                    |
+------------------+---------------------------------+
| creatoradrext    | Creator address                 |
+------------------+---------------------------------+
| creatoradrpcode  | Creator postal code             |
+------------------+---------------------------------+
| creatorcity      | Creator city                    |
+------------------+---------------------------------+
| creatorcountry   | Creator country                 |
+------------------+---------------------------------+
| creatoremailwrk  | Creator email                   |
+------------------+---------------------------------+
| creatorregion    | Creator state                   |
+------------------+---------------------------------+
| creatortelwrk    | Creator phone                   |
+------------------+---------------------------------+
| creatorurlwrk    | Creator website                 |
+------------------+---------------------------------+
| credate          | Date created                    |
+------------------+---------------------------------+
| credit           | Credit                          |
+------------------+---------------------------------+
| cretime          | Time created                    |
+------------------+---------------------------------+
| customfield1     | Custom field 1                  |
+------------------+---------------------------------+
| customfield2     | Custom field 2                  |
+------------------+---------------------------------+
| customfield3     | Custom field 3                  |
+------------------+---------------------------------+
| customfield4     | Custom field 4                  |
+------------------+---------------------------------+
| customfield5     | Custom field 5                  |
+------------------+---------------------------------+
| customfield6     | Custom field 6                  |
+------------------+---------------------------------+
| customfield7     | Custom field 7                  |
+------------------+---------------------------------+
| customfield8     | Custom field 8                  |
+------------------+---------------------------------+
| customfield9     | Custom field 9                  |
+------------------+---------------------------------+
| customfield10    | Custom field 10                 |
+------------------+---------------------------------+
| customfield11    | Custom field 11                 |
+------------------+---------------------------------+
| customfield12    | Custom field 12                 |
+------------------+---------------------------------+
| customfield13    | Custom field 13                 |
+------------------+---------------------------------+
| customfield14    | Custom field 14                 |
+------------------+---------------------------------+
| customfield15    | Custom field 15                 |
+------------------+---------------------------------+
| customfield16    | Custom field 16                 |
+------------------+---------------------------------+
| customfield17    | Custom field 17                 |
+------------------+---------------------------------+
| customfield18    | Custom field 18                 |
+------------------+---------------------------------+
| customfield19    | Custom field 19                 |
+------------------+---------------------------------+
| customfield20    | Custom field 20                 |
+------------------+---------------------------------+
| datesent         | Date sent                       |
+------------------+---------------------------------+
| editstatus       | edit status                     |
+------------------+---------------------------------+
| fixture          | Fixture identifier              |
+------------------+---------------------------------+
| headline         | Headline                        |
+------------------+---------------------------------+
| imagetype        | Image type                      |
+------------------+---------------------------------+
| intelgenre       | Intellectual genre              |
+------------------+---------------------------------+
| isocountrycode   | ISO country code                |
+------------------+---------------------------------+
| keyword          | Keywords                        |
+------------------+---------------------------------+
| label            | label                           |
+------------------+---------------------------------+
| language         | Language identifier             |
+------------------+---------------------------------+
| marked           | Marked                          |
+------------------+---------------------------------+
| objectname       | Object name                     |
+------------------+---------------------------------+
| orgprg           | Originating program             |
+------------------+---------------------------------+
| orgtransref      | Original transmission reference |
+------------------+---------------------------------+
| orientation      | Image orientation               |
+------------------+---------------------------------+
| prgver           | Program version                 |
+------------------+---------------------------------+
| rating           | Rating                          |
+------------------+---------------------------------+
| reldate          | Release date                    |
+------------------+---------------------------------+
| reltime          | Release time                    |
+------------------+---------------------------------+
| rightsusageterms | Rights usage terms              |
+------------------+---------------------------------+
| scene            | Scene                           |
+------------------+---------------------------------+
| source           | Source                          |
+------------------+---------------------------------+
| specinstr        | Special instructions            |
+------------------+---------------------------------+
| state            | Province/State                  |
+------------------+---------------------------------+
| subcategory      | Supplemental category           |
+------------------+---------------------------------+
| subfile          | Subfile                         |
+------------------+---------------------------------+
| subjectcode      | Subject code                    |
+------------------+---------------------------------+
| sublocation      | Sublocation                     |
+------------------+---------------------------------+
| timesent         | Time sent                       |
+------------------+---------------------------------+
| urgency          | Urgency                         |
+------------------+---------------------------------+
| usageterms       | Usage terms                     |
+------------------+---------------------------------+
| webstatement     | Copyright info URL              |
+------------------+---------------------------------+
