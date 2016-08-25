from db.db_keys import DBKeys
from db.doc_fetcher import MongoDocFetcher
from framework.voc_constants import PRODUCT_NAMES, TO_BE_TAGGED

def main(pidd, collection=PRODUCT_NAMES):

    # full_ts_docs = MongoDocFetcher(pidd, PRODUCT_NAMES)
    full_ts_docs = MongoDocFetcher(pidd, collection)
    articles = [doc[DBKeys.orig_words] for doc in full_ts_docs]
    xx = 66
    # res = custom_collocation(articles, win_size=6, run_trigram=True)
    # res2 = find_common_features(pidd, quant_to_return=25)
    # res4 = find_common_features_in_corpus(pidd, quant_to_return=5)


if __name__ == "__main__":
    # pidd = 'coffee'
    pidd = 'nescafe_facebook'
    collection = TO_BE_TAGGED
    main(pidd, collection=collection)