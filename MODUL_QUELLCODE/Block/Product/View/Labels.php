<?php
/**
 * Sbs_ComplianceLabels Magento 2 Extension
 *
 * @category  Sbs
 * @package   Sbs_ComplianceLabels
 * @author    Thomas Winkler <t.winkler.priv@gmail.com>
 * @copyright 2026 SBS
 */

namespace Sbs\ComplianceLabels\Block\Product\View;

use Magento\Framework\View\Element\Template;
use Magento\Framework\View\Element\Template\Context;
use Magento\Framework\Registry;
use Magento\Catalog\Model\Product;

class Labels extends Template
{
    /**
     * @var Registry
     */
    protected $registry;

    /**
     * @param Context $context
     * @param Registry $registry
     * @param array $data
     */
    public function __construct(
        Context $context,
        Registry $registry,
        array $data = []
    ) {
        $this->registry = $registry;
        parent::__construct($context, $data);
    }

    /**
     * Get current product
     *
     * @return Product|null
     */
    public function getProduct()
    {
        return $this->registry->registry('current_product');
    }

    /**
     * Get warranty years attribute value
     *
     * @return int
     */
    public function getWarrantyYears()
    {
        $product = $this->getProduct();
        if ($product) {
            return (int)$product->getData('manufacturer_warranty_years');
        }
        return 0;
    }

    /**
     * Get manufacturer attribute text/value
     *
     * @return string
     */
    public function getManufacturerName()
    {
        $product = $this->getProduct();
        if ($product) {
            $manufacturerText = $product->getAttributeText('manufacturer');
            if ($manufacturerText) {
                return $manufacturerText;
            }
            return (string)$product->getData('manufacturer');
        }
        return '';
    }

    /**
     * Get product model designation (or fallback to SKU)
     *
     * @return string
     */
    public function getProductModel()
    {
        $product = $this->getProduct();
        if ($product) {
            $model = $product->getData('model');
            if ($model) {
                return $model;
            }
            return $product->getSku();
        }
        return '';
    }
}
