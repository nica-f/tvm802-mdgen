
            # Mark image configuration
            outfile.write('Mark\n')
            outfile.write('0\n')
            outfile.write('2\n')
            outfile.write('False\n')
            outfile.write('6\n')
            outfile.write('150\n')
            # two Marks image data, base64 encoded, 8 bit raw bitmap,
            # size varies with selected mark size, formula unclear yet 2.5mm mark will become 208x208 pixel
            #for i in range (0, 44240, 1):
            #    outfile.write('A')
            #outfile.write('\n')
            #for i in range (0, 44240, 1):
            #    outfile.write('A')
            #outfile.write('\n\n')
            outfile.write('\n')

            # IC stack config, 30 positions each
            outfile.write('IC\n')
            for i in range (1, 31, 1):
                outfile.write('0.00\n')
            outfile.write('\n')
            for i in range (1, 31, 1):
                outfile.write('0.00\n')
            outfile.write('\n')
            for i in range (1, 31, 1):
                outfile.write('0.00\n')
            outfile.write('\n')
            for i in range (1, 31, 1):
                outfile.write('0.00\n')
            outfile.write('\n')

            for i in range (1, 31, 1):
                outfile.write('1\n')
            outfile.write('\n')

            for i in range (1, 31, 1):
                outfile.write('1\n')
            outfile.write('\n')

            # IC stack names
            for i in range (1, 31, 1):
                outfile.write('\n')
            for i in range (1, 31, 1):
                outfile.write('0\n')
            for i in range (1, 31, 1):
                outfile.write('0\n')
            outfile.write('\n')
            for i in range (1, 31, 1):
                outfile.write('0\n')
            outfile.write('\n')
            for i in range (1, 31, 1):
                outfile.write('0\n')
            outfile.write('\n')
            for i in range (1, 31, 1):
                outfile.write('0.1\n')
            outfile.write('\n')

            outfile.write('PCB\n')
            outfile.write('1\n')
            outfile.write('1\n')
            outfile.write('\n')
            outfile.write('True\n')
            outfile.write('\n')
            outfile.write('0\n')
            outfile.write('\n')
            outfile.write('0\n')
            outfile.write('\n')
            outfile.write('0\n')
            outfile.write('\n')
            outfile.write('0.00\n')
            outfile.write('0.00\n')
            outfile.write('0.00\n')
            outfile.write('0.00\n')
            outfile.write('0.00\n')
            outfile.write('0.00\n')

            outfile.write('Stack\n')
            for i in range (1, 31, 1):
                outfile.write('CL%02d' %i + '\n')
            for i in range (1, 31, 1):
                outfile.write('CB%02d' %i + '\n')
            outfile.write('\n')

            for i in range (1, 31, 1):
                outfile.write('0\n')
            for i in range (1, 31, 1):
                outfile.write('0\n')
            outfile.write('\n')

            for i in range (1, 31, 1):
                outfile.write('0\n')
            for i in range (1, 31, 1):
                outfile.write('0\n')
            outfile.write('\n')

            # height
            for i in range (1, 31, 1):
                outfile.write('0.1\n')
            for i in range (1, 31, 1):
                outfile.write('0.1\n')
            outfile.write('\n')

            # pick angle
            for i in range (1, 31, 1):
                outfile.write('90\n')
            for i in range (1, 31, 1):
                outfile.write('0\n')
            outfile.write('\n')

            # comp threshold
            for i in range (1, 31, 1):
                outfile.write('50\n')
            for i in range (1, 31, 1):
                outfile.write('50\n')
            outfile.write('\n')
