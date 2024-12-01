/** @odoo-module **/

import { ProductInfoPopup } from "@point_of_sale/app/utils/product_info_popup/product_info_popup";
import { patch } from "@web/core/utils/patch";

patch(ProductInfoPopup, {
    setup() {
        super.setup();
        console.log('Product Data:', {
            product: this.props.product,
            location: this.props.product.location_name
        });
    },

    get productDetails() {
        const details = super.productDetails || [];
        if (this.props.product.location_name) {
            details.push({
                label: 'Stock Location',
                value: this.props.product.location_name,
            });
        }
        return details;
    },
});