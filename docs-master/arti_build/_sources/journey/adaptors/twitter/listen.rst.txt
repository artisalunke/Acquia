.. include:: /common/global.rst

Twitter: Listen adaptor
=======================

The Twitter Listen Adaptor allows a graph to listen for `user stream
messages <https://dev.twitter.com/streaming/overview/messages-types#user_stream_messsages>`__
for the authenticated user. These include Tweets that contain keywords,
hashtags or usernames and events that include friends lists, direct
messages and many other event types.

Creating the adaptor
--------------------

To create the Twitter listen adaptor on any graph, complete the
following actions:

.. note::
    To create a Twitter listen adaptor it is best practice, but not
    necessary, to create a `database
    connection </journey/connect/database>`__.

#. Click **Add** in the top right of a graph window.
   This will display the Listener configuration dialog.
#. In the **Listener Type** list, click **Twitter**.
#. In the **Adaptor Connection (Environment)** list, either click the
   connection that you want to use or edit it directly by clicking the
   pencil icon next to the connection name
#. In the **Twitter Listen Mode** list, click either **Keywords** or
   **User Stream**.

   -  *Keywords listen mode*
      In this mode the Listener will connect to the Twitter streaming
      API and find any tweet texts, hashtags or mentions of usernames
      that match the specified `tracking
      phrases <https://dev.twitter.com/streaming/overview/request-parameters#track>`__.

          The tracking phrase is a comma-separated list of phrases which
          will be used to determine what Tweets will be delivered on the
          stream. A phrase may be one or more terms separated by spaces,
          and a phrase will match if all of the terms in the phrase are
          present in the Tweet, regardless of order and ignoring case.
          By this model, you can think of commas as logical ORs, while
          spaces are equivalent to logical ANDs (e.g. ``the twitter`` is
          ``the AND twitter``, and ``the,twitter`` is
          ``the OR twitter``).

      The returned values will be a `Twitter tweet
      object <https://dev.twitter.com/overview/api/tweets>`__.

   -  *User event stream mode*
      In this mode the Listener will connect to the User Stream for the
      authorized user and return the `user stream
      messages <https://dev.twitter.com/streaming/overview/messages-types#user_stream_messsages>`__
      as defined in the Twitter API. You can choose one or more of the
      outputs to receive:

      -  **Events** - Notifications about non-Tweet events, which
         includes Like and Unlike events.
      -  **Friends** - Upon establishing a User Stream connection,
         Twitter will send a preamble before starting regular message
         delivery. This preamble contains a list of the user’s friends.
         This is represented as an array of user ids
      -  **Direct Messages** - Returns `direct message
         objects <https://dev.twitter.com/rest/reference/get/direct_messages/show>`__
         as defined in the Twitter API.
      -  **Tweet** - Any Tweets from the user.

#. Click **Save**.

Validation warnings
-------------------

Attempting to save the Database Listen Adaptor without completing all of
the necessary parts will create one or more notification:

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Twitter Listener must have a    | No connection has been selected   |
| Connection set**                  |                                   |
+-----------------------------------+-----------------------------------+
| **Twitter Listener must have an   | The twitter listener needs a      |
| output destination set**          | location to write the incoming    |
|                                   | records to for all of the output  |
|                                   | types                             |
+-----------------------------------+-----------------------------------+
| **Twitter Keyword Listener must   | In order to track phrases the     |
| have a keywords tracking phrase** | keywords tracking phrase must not |
|                                   | be empty                          |
+-----------------------------------+-----------------------------------+
