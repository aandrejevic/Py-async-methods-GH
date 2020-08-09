try:
    import sys
    import time
    start = time.time()

    print 'Importing rhinoinside'
    import rhinoinside
    rhinoinside.load()
    import Rhino
    print 'Rhino loaded at %s sec' % (time.time() - start)
    
    from ostate.util import rhino_json


    _input = sys.argv[1]
    _output = sys.argv[2]

    # The main function
    def process(input, output):
        mesh = rhino_json.deserialize(file=input)
        mesh = mesh.Offset(-5.0)
        rhino_json.serialize(mesh, file=output)
        
    process(_input, _output)
    print 'Finished processing at %s sec' % (time.time() - start)

except Exception, e:
    print e

time.sleep(3)
