__author__ = 'Quintin Martinus'


def dayplan(kcalls, kcallsburned, studyhours):
    print "This is how well or bad you did today!"
    print "Today you consumed %r calories." % kcalls
    print "Furthermore, you burned %r calories through exercise." % kcallsburned
    print "Finally, you studied for %r hours!" % studyhours
    print "Revise how you did and plan your adaptions for tomorrow."


print "How many calories did you consume today?"
kcalls = int(raw_input()) # asks for input and converts input into integers

print "How many calories did you burn today with exercise?"
kcallsburned = int(raw_input())

print "And finally, How many hours did you study today?"
studyhours = int(raw_input())

dayplan(kcalls, kcallsburned, studyhours)
