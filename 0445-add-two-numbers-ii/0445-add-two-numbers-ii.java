/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode prevL1 = null;
        ListNode currentL1 = l1;
        while (currentL1 != null) {
            ListNode temp = currentL1.next;
            currentL1.next = prevL1;
            prevL1 = currentL1;
            currentL1 = temp;
        }

        ListNode prevL2 = null;
        ListNode currentL2 = l2;
        while (currentL2 != null) {
            ListNode temp = currentL2.next;
            currentL2.next = prevL2;
            prevL2 = currentL2;
            currentL2 = temp;
        }

        if (prevL1 == null) return prevL2;
        if (prevL2 == null) return prevL1;

        ListNode dummy = new ListNode(0);
        ListNode newList = dummy;
        int carry = 0;

        while (prevL1 != null || prevL2 != null || carry != 0) {
            int val1 = (prevL1 != null) ? prevL1.val : 0;
            int val2 = (prevL2 != null) ? prevL2.val : 0;

            int sum = val1 + val2 + carry;
            carry = sum / 10;
            newList.next = new ListNode(sum % 10);

            newList = newList.next;
            if (prevL1 != null) prevL1 = prevL1.next;
            if (prevL2 != null) prevL2 = prevL2.next;
        }

        ListNode prevNew = null;
        ListNode currentNew = dummy.next;
        while (currentNew != null) {
            ListNode temp = currentNew.next;
            currentNew.next = prevNew;
            prevNew = currentNew;
            currentNew = temp;
        }

        return prevNew;
    }
}