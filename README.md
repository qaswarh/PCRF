# PCRF with Pandas
This repo will discuss how python can query pandas to analyze saved text files from Wireshark

Export Packet Disections As Plain Text.. from the File pull down menu in Wireshark
The lower part of the poped-up window would look: 

![pcaptxt](https://user-images.githubusercontent.com/47313728/149603698-df894d38-7379-4f5b-8a78-753958999416.PNG)

![PCRF Architecture](https://user-images.githubusercontent.com/47313728/149600160-c0372717-eda8-41dd-89f7-c55c13923044.PNG)

Let have a pcrf**if**.txt from a pcap of Gx **i**nter**f**ace and query the Pandas to find the number of AVPs which are not Mandatory but we use in **EPC** network

Let's use the following lines to query

![GxNMA](https://user-images.githubusercontent.com/47313728/153114878-fe9ea3b9-5d67-465c-8610-fe9495319e67.PNG)

And the result from a small file:

![NMAGx](https://user-images.githubusercontent.com/47313728/153115229-8e842dd1-7b65-4359-bfda-dbe56b4716a1.PNG)
