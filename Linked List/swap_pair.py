
# swap pair with complete node


"""
    Method 1:

        1) start with curr=head , prev =none , nex = none, i=0
        2) while curr is not none and curr.next is not none
        3) nex = curr.next
        4) check if i is divided by 2
        5) if yes then check if prev and prev.next is none if yes head = nex else prev.next = nex
        6) curr.next = nex.next
        7) nex.next = curr      swap two nodes
        8) prev =curr
        9) curr = curr.next


"""




def pairWiseSwap(self, head):
        # code here
        curr = head
        prev = None
        nex = None

        i = 0
        while(curr is not None and curr.next!= None):
            nex = curr.next
            if i%2 == 0:
                if prev and prev.next:
                    prev.next = nex
                else:
                    head= nex
                curr.next = nex.next
                nex.next = curr

            prev = curr
            curr = curr.next

        return head
