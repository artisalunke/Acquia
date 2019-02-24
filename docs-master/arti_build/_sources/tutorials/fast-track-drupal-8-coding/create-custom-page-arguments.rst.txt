.. include:: /common/global.rst

Create a custom page with arguments
===================================

| **Fast Track to Drupal 8 Coding** – *`Back to
  Intro </tutorials/fast-track-drupal-8-coding>`__*
| *Previous lesson – `Create a custom
  page </tutorials/fast-track-drupal-8-coding/create-custom-page>`__*  |  *Next
  lesson – `Create nodes
  programmatically </tutorials/fast-track-drupal-8-coding/create-nodes-programmatically>`__*

Lesson Goal
-----------

Create a custom page at ``/offers/hot/%`` that displays content based on
arguments.

Implementation Method
---------------------

+-----------------------------------+-----------------------------------+
| Drupal Version                    | Method                            |
+===================================+===================================+
| Drupal 7                          | Use                               |
|                                   | `hook_menu() <https://api.drupal. |
|                                   | org/api/drupal/modules%21system%2 |
|                                   | 1system.api.php/function/hook_men |
|                                   | u/7.x>`__                         |
+-----------------------------------+-----------------------------------+
| Drupal 8                          | Use `lotus.routing.yml            |
|                                   | file <https://www.drupal.org/docs |
|                                   | /8/creating-custom-modules/add-a- |
|                                   | routing-file>`__                  |
+-----------------------------------+-----------------------------------+

Drupal 7 method
---------------

Add the following code to the ``lotus.module`` file:

``/** * Implements hook_menu() **/  function lotus_menu() {     $items['offers/hot/%'] = array(       'title' => 'Offers Galore!',       'description' => 'Landing Page for Offers Page',       'page callback' => 'lotus_offers_page',       'page arguments' => array(1),       'access arguments' => array('access content')     );     return $items;   }  /**  * Page callback function **/    function 'lotus_offers_page'($count) {     return 'You will get ' . $count . '% discount!!' ;   }``

Drupal 8 method
---------------

Add the following code to the ``lotus.routing.yml`` file:

``lotus.offers_controller_hello:   path: '/offers/hot/{count}'   defaults:     _controller: '\Drupal\lotus\Controller\OffersController::hello'     _title: 'Offers'   requirements:     _permission: 'access content'``

Add the following code to the
``lotus/src/Controller/OffersController.php`` file:

``namespace Drupal\lotus\Controller;  use Drupal\Core\Controller\ControllerBase;  /**  * Class OffersController.  *  * @package Drupal\lotus\Controller  */ class OffersController extends ControllerBase {    /**    * Hello.    *    * @return string    *   Return Hello string.    */   public function hello($count) {     return [       '#type' => 'markup',       '#markup' => $this->t('You will get %count% discount!!', array('%count' => $count)),     ];   }  }``

Gist Link
---------

https://gist.github.com/gargsuchi/f1e7276f26c7d152f74b295ca586df73

Resources
---------

https://www.drupal.org/docs/8/api/routing-system/using-parameters-in-routes 
