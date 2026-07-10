/**
 * Sbs_ComplianceLabels Magento 2 Extension
 *
 * @category  Sbs
 * @package   Sbs_ComplianceLabels
 * @author    Thomas Winkler <t.winkler.priv@gmail.com>
 * @copyright 2026 SBS
 */

define([
    'jquery'
], function ($) {
    'use strict';

    return function (config, element) {
        var $element = $(element);
        var $trigger = $element.find('.garan-trigger');

        $trigger.on('click', function () {
            var isActive = $element.toggleClass('active').hasClass('active');
            $trigger.attr('aria-expanded', isActive ? 'true' : 'false');
        });
    };
});
