import asyncio
class PuppetRecorder():
    def __init__(self, frequency=100):
        
        # List of functions and variables to be used as inputs
        self.inputs = []

        # Recording frequency (Hz)
        self.recFreq = frequency

        # Recording flag
        self.recording = False
    
    def add_input(self, input):

        # Add input to list of inputs
        self.inputs.append(input)

    #TODO: Find the best way to implement this
    #def set_storage(self, storage):

    #def save_data(self, data, index):

    async def start_recording(self):

        # Start recording
        self.recording = True
        # TODO: create new file

    
        # Start timer interrupt
        while self.recording:
            for i in range(len(self.inputs)):
                # Record input
                if self.inputs[i].type() == function:
                    # Record function output
                    data = self.inputs[i]()

                else:
                    # Record variable value
                    data = self.inputs[i]
                # Save data
                #self.save_data(data, i)
            await asyncio.sleep(1/self.recFreq)

    def stop_recording(self):
        # Stop recording
        self.recording = False



    
