// PROBLEM:
//   Using C++ and only using the STL stack class (#include <stack>), design a
//   queue class (a.k.a. FIFO). You can only #include the <stack> class, nothing
//   else.
//
// Author: Milad Mohammadi

#include <stack>

class queue : public stack {
    public:
        queue () {}
        ~queue () {}

        void push (int elem) {
            _in.push (elem);
        }

        int pop () {
            in_to_out_swap ();
            int front = _out.pop ();
            out_to_in_swap ();
            return front;
        }

        int front () {
            in_to_out_swap ();
            int front = _out.top ();
            out_to_in_swap ();
            return front;
        }

        int back () {
            return _in.top ();
        }

        bool empty () {
            if (_in.empty ()) 
                return true;
            return false;
        }

        int size () {
            return _in.size ();
        }

    private:
        void out_to_in_swap () {
            stack<int>::iterator it;
            for (it = _out.begin (); it != _out.end (); it++) {
                _in.push(*it);
            }
            while (!_out.empty ()) {
                _out.pop ();
            }
        }
        void in_to_out_swap () {
            stack<int>::iterator it;
            for (it = _in.begin (); it != _in.end (); it++) {
                _out.push (*it);
            }
            while (!_in.empty ()) {
                _in.pop ();
            }
        }

    privte:
        stack<int> _in;
        stack<int> _out;
};
