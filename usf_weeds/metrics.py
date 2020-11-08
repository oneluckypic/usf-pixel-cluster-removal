

from usf_weeds.labels import chip_image


def simple_accuracy(labels_df, mask):

    masked_chips = chip_image(mask, labels_df[labels_df['class'] != 'Background'])
    visible_chips = chip_image(mask, labels_df[labels_df['class'] == 'Background'])

    num_masked = sum([(masked == 0).sum() for masked in masked_chips])
    num_visible = sum([(visible > 0).sum() for visible in visible_chips])

    size_masked = sum([masked.shape[0] * masked.shape[1] for masked in masked_chips])
    size_visible = sum([visible.shape[0] * visible.shape[1] for visible in visible_chips])
    
    metric = (num_masked / size_masked + num_visible / size_visible) / 2.0
    return metric
