.data
.asciiz %d; \00: 
.asciiz %f; \00: 
double1: .double 1.000000e+01
.asciiz %d; \00: 
.asciiz %f; \00: 
double2: .double 1.000000e+01
.asciiz %d; \00: 
.asciiz %f; \00: 
double3: .double 1.000000e+01
.asciiz %d; \00: 
.asciiz %f; \00: 
double4: .double 1.000000e+01
.globl main
.text
                
main:   
        addiu   $sp,$sp, -4
        sw      $fp,4($sp)
        move    $fp,$sp
        la      $6,string1
        li      $6,10
        li      $6,10
        li      $v0,1
        syscall 
        la      $6,string2
        l.d     $None,double1
        l.d     $None,double1
        li      $v0,3
        syscall 
        la      $6,string3
        li      $6,10
        li      $6,10
        li      $v0,1
        syscall 
        la      $6,string4
        l.d     $None,double2
        l.d     $None,double2
        li      $v0,3
        syscall 
        la      $6,string5
        li      $6,10
        li      $6,10
        li      $v0,1
        syscall 
        la      $6,string6
        l.d     $None,double3
        l.d     $None,double3
        li      $v0,3
        syscall 
        la      $6,string7
        li      $6,10
        li      $6,10
        li      $v0,1
        syscall 
        la      $6,string8
        l.d     $None,double4
        l.d     $None,double4
        li      $v0,3
        syscall 
        nop     
        move    $sp,$fp
        lw      $fp,4($sp)
        addiu   $sp,$sp,8
        li      $v0,10
        syscall 