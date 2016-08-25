# README #

### What is this algorithm? ###

* It is based on the original collocations algorithm with a small but important different. Collocations are based on a sliding window while fixed collocations are based on a 
fixed index and an additional sliding index. 

### What is this algorithm used for? ###
* Iv'e originally created this algorithm to identify products' models. In most cases a product description begins with the brand name and right after the brand name you'll see
the product model.

* Example - Model extraction:
	---Let's have a look at some products descriptions---
	input_text1 = 'Apple iPhone 6 32 GB White'
	input_text2 = 'Apple iPhone 6 64 GB White'
	input_text3 = 'Apple iPhone 6 32 GB Black'
	input_text3 = 'Apple iPhone 6s 32 GB Black'
	input_text3 = 'Apple iPhone 6s 64 GB Black'
	
	In this example the outputs we are looking for are - iPhone 6 and iPhone 6s (for a small selected window)
	Right after we find the brand name ('Apple' in that case) the algorithm will do the followings:
		iPhone 6, iPhone 32, iPhone GB, iPhone White, iPhone 6 32, iPhone 6 GB, iPhone 6 White, iPhone 6 32 GB, iPhone 6 32 White...
		iPhone 6, iPhone 64, iPhone GB, iPhone White...
		iPhone 6, iPhone 32, iPhone GB, iPhone Black...
		iPhone 6s, iPhone 32, iPhone GB, iPhone Black...
		iPhone 6s, iPhone 64, iPhone GB, iPhone Black...
		
	Now all that left is count each n-gram and return it.
		
### What if I want to use this? ###

* No problem, just contact me at cijalm@gmail.com first.
