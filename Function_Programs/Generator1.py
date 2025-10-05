def number_generator():
    for i in range(5):
        yield i

gen = number_generator()

for num in gen:
    print(num)
    
    '''return	                                yield
Exits the function immediately	        Pauses the function and resumes later
Returns a value	                        Yields a value to the caller (like an iterator)
No further execution after return	    Execution continues from where it left off'''


'''Concept  	Purpose	                                                 Key Keyword	            Example Use Case
Decorator	    Modifies/enhances behavior of a function	             @decorator         	Logging, authorization, timing
Generator	    Creates an iterator that yields one value at a time 	 yield	                Large file processing, streaming 
                                                                                                    data'''