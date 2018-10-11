def initialize(context):  
    context.spy = sid(21329)  
    context.order_id = None  
    context.first_bar = False  
    context.bar_count = 0  
    set_slippage(slippage.VolumeShareSlippage(volume_limit=1e-5, price_impact=0))

def handle_data(context, data):  
    context.bar_count += 1

    if not context.first_bar:  
        context.order_id = order(context.spy,100)  
        print context.order_id  
        context.first_bar = True  
    print get_order(context.order_id)  
    print get_order(context.order_id).dt # datetime stamp, order completely filled or cancelled  
    print get_order(context.order_id).filled # cumulative number of shares filled  
    print context.portfolio.positions[context.spy]  
    if context.bar_count == 5:  
        cancel_order(context.order_id)  
