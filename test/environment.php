<?php
/**
 * Create file environment.php and copy contents of this file to environment.php
 */

//define('ENVIRONMENT', 'unit_testing');
//define('ENVIRONMENT', 'development2');
define('ENVIRONMENT', 'development');

/* making the variable available for error 500 handler in all cases */
$GLOBALS['ENVIRONMENT'] = ENVIRONMENT;
